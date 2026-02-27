# CI/CD Pipeline Security Review

This checklist covers security review of CI/CD pipeline configurations across GitHub Actions, GitLab CI, Jenkins, Azure DevOps, and general pipeline definitions. Use it to evaluate pipeline files for secrets exposure, supply chain risks, insufficient access controls, and missing security scanning before pipelines are activated or modified.

---

## Critical Severity

These findings represent immediate risks that could lead to secret compromise, supply chain attacks, or unauthorized production deployments.

### Secrets Handling

- [ ] **Secrets printed or exposed in build logs**
  - What to look for: Pipeline steps that echo, print, or log environment variables containing secrets. Check for `echo $SECRET`, `env` or `printenv` commands, debug flags that dump environment, and logging frameworks that serialize the full environment context.
  - Why it matters: Build logs are often accessible to all repository contributors and may be retained indefinitely. Exposed secrets in logs require immediate rotation and are a common source of credential compromise.

- [ ] **Secrets stored in pipeline configuration files rather than a secrets manager**
  - What to look for: Hardcoded API keys, passwords, tokens, or connection strings in `.github/workflows/*.yml`, `.gitlab-ci.yml`, `Jenkinsfile`, or `azure-pipelines.yml` files.
  - Why it matters: Pipeline configuration files are committed to version control and visible to anyone with repository read access. Secrets in these files persist permanently in git history.

- [ ] **Secrets accessible to pull request workflows from forks**
  - What to look for: GitHub Actions workflows triggered by `pull_request_target` that checkout the fork's code and have access to repository secrets. Also check for `pull_request` triggers on public repos where secrets are available.
  - Why it matters: Attackers can fork a public repository, modify workflow files to exfiltrate secrets, and open a pull request. The `pull_request_target` event runs in the context of the base repository with full secret access.

### Access Control

- [ ] **Self-hosted runners with excessive host-level permissions**
  - What to look for: Self-hosted GitHub Actions runners, GitLab runners, or Jenkins agents running as root, with Docker socket access, or on shared infrastructure without proper isolation between jobs.
  - Why it matters: Self-hosted runners execute arbitrary code from pipeline definitions. A compromised runner with elevated permissions provides persistent access to the host, network, and potentially other jobs' secrets.

- [ ] **Pipeline can modify its own workflow files and trigger itself**
  - What to look for: Workflows with write permissions to the repository that can modify `.github/workflows/`, `.gitlab-ci.yml`, or `Jenkinsfile` and then trigger new pipeline runs, creating a self-modification loop.
  - Why it matters: This enables privilege escalation: a contributor can submit a change that modifies the pipeline to bypass required checks, exfiltrate secrets, or deploy malicious code.

### Build Integrity

- [ ] **Artifact or container images pushed without integrity verification**
  - What to look for: Build steps that push container images, packages, or binaries to registries or artifact stores without generating checksums, signatures, or attestations.
  - Why it matters: Without integrity verification, there is no way to confirm that deployed artifacts match what was built. Tampered artifacts in transit or at rest can introduce malicious code.

---

## High Severity

These findings represent significant risks related to supply chain security, insufficient scanning, and deployment controls.

### Dependency Management

- [ ] **No pinned versions on third-party actions, plugins, or images**
  - What to look for: GitHub Actions using `uses: actions/checkout@main` instead of `uses: actions/checkout@v4.1.1` or a commit SHA. GitLab CI images using `image: node:latest`. Jenkins plugins without version pins.
  - Why it matters: Unpinned dependencies allow upstream maintainers (or compromised accounts) to inject malicious code that automatically executes in your pipeline. Pin to specific versions or commit SHAs.

- [ ] **No dependency vulnerability scanning (SCA) in the pipeline**
  - What to look for: Missing steps for tools like `npm audit`, `pip-audit`, Snyk, Dependabot, Trivy, or Grype that check application and container image dependencies for known vulnerabilities.
  - Why it matters: Known vulnerabilities in dependencies are the most common attack vector. Without automated scanning, vulnerable dependencies are deployed without detection.

- [ ] **No SAST (Static Application Security Testing) in the pipeline**
  - What to look for: Missing static analysis steps using tools like Semgrep, CodeQL, SonarQube, Bandit, or ESLint security plugins.
  - Why it matters: SAST catches common vulnerability patterns (injection, auth bypass, insecure crypto) before code reaches production. Without it, these defects rely solely on manual code review.

### Deployment Controls

- [ ] **No required approvals or manual gates for production deployments**
  - What to look for: Pipelines that deploy directly to production on merge without environment protection rules, required reviewers, or manual approval steps.
  - Why it matters: Without deployment gates, any merged change (including compromised dependencies or accidental misconfigurations) is automatically deployed to production without human verification.

- [ ] **No separation between build and deploy credentials**
  - What to look for: A single set of credentials or service principal used for both building artifacts and deploying to production, rather than separate least-privilege identities for each stage.
  - Why it matters: If build credentials can also deploy, a compromised build step can push arbitrary code to production. Separation limits the blast radius of any single credential compromise.

- [ ] **No rollback mechanism defined in the pipeline**
  - What to look for: Deployment pipelines without automated rollback steps, health checks, or references to a rollback procedure when deployment validation fails.
  - Why it matters: Without rollback capability, a failed or compromised deployment remains in production while teams manually intervene, extending the window of exposure.

### Artifact Security

- [ ] **Container images not scanned for vulnerabilities before push**
  - What to look for: Docker build and push steps without intermediate vulnerability scanning using Trivy, Grype, Snyk Container, or equivalent tools.
  - Why it matters: Container images may contain OS-level and library-level vulnerabilities. Scanning before push prevents deploying images with known critical CVEs.

- [ ] **Artifacts published to public registries by default**
  - What to look for: Pipeline configurations that push packages to public npm, PyPI, Docker Hub, or Maven Central without explicit scoping to a private registry.
  - Why it matters: Accidental publication of internal packages to public registries exposes proprietary code, and may expose internal API endpoints, credentials, or business logic.

### Access Control

- [ ] **No branch protection rules on main/production branches**
  - What to look for: Repository settings allowing direct pushes to `main`, `master`, or release branches without requiring pull requests, status checks, or code review.
  - Why it matters: Without branch protection, any contributor can push directly to the production branch, bypassing code review, security scanning, and approval workflows.

- [ ] **Overly broad GITHUB_TOKEN or CI_JOB_TOKEN permissions**
  - What to look for: GitHub Actions workflows without explicit `permissions` block (defaulting to broad read-write), or with `permissions: write-all`. GitLab jobs with `CI_JOB_TOKEN` access to unrelated projects.
  - Why it matters: The default token often has write access to repository contents, packages, and deployments. Restricting permissions to the minimum needed limits damage from compromised workflows.

---

## Medium Severity

These findings represent defense-in-depth gaps in pipeline security configuration.

### Secrets Handling

- [ ] **No secret rotation process or documentation**
  - What to look for: Pipeline secrets (repository secrets, variable groups, Jenkins credentials) without documented rotation schedules or automated rotation.
  - Why it matters: Long-lived secrets in CI/CD systems accumulate risk over time. Without rotation, a compromised secret remains valid indefinitely until manually changed.

- [ ] **Secrets shared across environments (dev/staging/production)**
  - What to look for: The same secret names and values used in development, staging, and production pipeline configurations without environment-specific scoping.
  - Why it matters: Shared secrets mean that compromise of a lower environment's pipeline also compromises production credentials, eliminating environment isolation benefits.

### Build Integrity

- [ ] **No reproducible builds or build environment pinning**
  - What to look for: Builds that depend on mutable base images, dynamic dependency resolution (no lockfiles used), or tools installed from `curl | bash` patterns during build time.
  - Why it matters: Non-reproducible builds make it impossible to verify that a given artifact corresponds to a specific set of source code, undermining auditability and tamper detection.

- [ ] **Cache poisoning risks in shared build caches**
  - What to look for: Pipeline caches (npm cache, pip cache, Docker layer cache) shared across branches or contributors without integrity verification.
  - Why it matters: A malicious contributor can poison the build cache on a feature branch, and the poisoned cache will be used by subsequent builds on the main branch, injecting malicious dependencies.

### Deployment Controls

- [ ] **No environment-specific pipeline configurations**
  - What to look for: A single pipeline definition used for all environments without conditional logic for environment-specific security controls, approvals, or configurations.
  - Why it matters: Production deployments should have stricter controls than development. Uniform pipelines apply the same (often minimal) controls to all environments.

- [ ] **No deployment frequency or change window controls**
  - What to look for: Pipelines that can deploy to production at any time without blackout windows, change freeze awareness, or rate limiting on deployments.
  - Why it matters: Uncontrolled deployment timing can result in changes during high-risk periods (incidents, maintenance windows) when monitoring may be reduced and teams unavailable.

### Access Control

- [ ] **Third-party CI/CD integrations with excessive repository access**
  - What to look for: OAuth apps, GitHub Apps, or GitLab integrations used by CI/CD tools with access to all repositories rather than specific ones, or with write permissions when only read is needed.
  - Why it matters: Over-privileged integrations expand the attack surface. Compromise of the third-party service grants access to all repositories, not just those the integration actually needs.

- [ ] **No audit logging of pipeline configuration changes**
  - What to look for: Missing audit trail for changes to pipeline secrets, environment variables, runner configurations, or deployment environment settings.
  - Why it matters: Without audit logs, unauthorized modifications to pipeline security controls cannot be detected or attributed, enabling persistent backdoors.

- [ ] **Pipeline triggers not restricted to authorized events**
  - What to look for: Workflows that trigger on broad events like `push` to all branches, `issue_comment`, `workflow_dispatch` without input validation, or cron schedules without freshness checks.
  - Why it matters: Overly broad triggers increase the attack surface by allowing pipeline execution from unexpected contexts, potentially with different security assumptions.

### Dependency Management

- [ ] **No DAST (Dynamic Application Security Testing) in the pipeline**
  - What to look for: Missing post-deployment scanning steps using tools like OWASP ZAP, Nuclei, Burp Suite CI, or equivalent dynamic analysis.
  - Why it matters: DAST catches runtime vulnerabilities (auth bypass, SSRF, header injection) that static analysis cannot detect, providing defense-in-depth for deployed applications.

---

## Low Severity

These findings represent best-practice improvements and supply chain hardening.

### Build Integrity

- [ ] **No build provenance or SLSA attestation**
  - What to look for: Missing SLSA (Supply-chain Levels for Software Artifacts) provenance generation, such as `slsa-github-generator`, Sigstore, or in-toto attestations attached to build artifacts.
  - Why it matters: Build provenance cryptographically links artifacts to their source code and build process, enabling consumers to verify that artifacts were built from expected source by expected infrastructure.

- [ ] **No SBOM (Software Bill of Materials) generated during builds**
  - What to look for: Missing SBOM generation steps using tools like Syft, CycloneDX, or SPDX generators as part of the container or application build process.
  - Why it matters: SBOMs enable rapid vulnerability assessment when new CVEs are disclosed, allowing teams to determine exposure without rebuilding or re-scanning.

### Operational Security

- [ ] **No pipeline execution timeout configured**
  - What to look for: Jobs or steps without `timeout-minutes` (GitHub Actions), `timeout` (GitLab CI), or equivalent time limits.
  - Why it matters: Without timeouts, hung or malicious jobs can consume runner resources indefinitely, causing denial of service to other pipeline jobs and accumulating compute costs.

- [ ] **No notification on pipeline security scan failures**
  - What to look for: Security scanning steps that run but do not send alerts (Slack, email, PagerDuty) when critical or high vulnerabilities are found, relying on developers to check build results.
  - Why it matters: Without active notification, security findings are passively ignored. Alert integration ensures security issues receive prompt attention.

- [ ] **No pipeline for infrastructure drift detection**
  - What to look for: Missing scheduled pipeline runs that compare actual infrastructure state to declared IaC state using `terraform plan`, `pulumi preview`, or equivalent drift detection tools.
  - Why it matters: Infrastructure drift indicates unauthorized manual changes that may weaken security controls. Regular drift detection ensures IaC remains the source of truth.
