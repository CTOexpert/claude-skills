# Kubernetes Security Review

This checklist covers security review of Kubernetes manifests, Helm charts, RBAC configurations, network policies, and admission control settings. Use it to evaluate workload definitions, cluster configuration, and operational security before deploying to shared or production clusters.

---

## Critical Severity

These findings represent immediate risks that could lead to cluster compromise, container escape, or exposure of sensitive data.

### Pod Security

- [ ] **Containers running as root (UID 0)**
  - What to look for: Pod specs missing `securityContext.runAsNonRoot: true` or explicitly setting `runAsUser: 0`. Check both pod-level and container-level security contexts.
  - Why it matters: Root inside a container is root on the host if a container escape vulnerability exists. Running as non-root is the single most impactful container hardening measure.

- [ ] **Privileged containers enabled**
  - What to look for: `securityContext.privileged: true` on any container spec.
  - Why it matters: Privileged containers have full access to host devices and kernel capabilities, effectively disabling all container isolation. A privileged container is equivalent to root on the host.

- [ ] **hostNetwork, hostPID, or hostIPC enabled**
  - What to look for: Pod specs with `hostNetwork: true`, `hostPID: true`, or `hostIPC: true`.
  - Why it matters: These settings break namespace isolation. `hostNetwork` exposes the pod to the host network stack (bypassing NetworkPolicy). `hostPID` allows viewing and signaling host processes. `hostIPC` shares inter-process communication with the host.

- [ ] **Containers mounting the Docker socket or containerd socket**
  - What to look for: Volume mounts for `/var/run/docker.sock`, `/var/run/containerd/containerd.sock`, or `/run/containerd/containerd.sock`.
  - Why it matters: Access to the container runtime socket allows arbitrary container creation on the host, enabling full cluster compromise through container escape and lateral movement.

- [ ] **hostPath volumes mounting sensitive host directories**
  - What to look for: `hostPath` volumes mounting `/`, `/etc`, `/var`, `/root`, `/home`, or other sensitive host filesystem paths.
  - Why it matters: Host filesystem access allows reading secrets, modifying system configuration, and potentially escalating to host-level access.

### RBAC

- [ ] **ClusterRoleBindings granting cluster-admin to service accounts or broad groups**
  - What to look for: `ClusterRoleBinding` resources binding `cluster-admin` to service accounts, user groups, or any non-human identity used by applications.
  - Why it matters: `cluster-admin` grants unrestricted access to every resource in every namespace. A compromised workload with this binding can take full control of the cluster.

- [ ] **RBAC roles with wildcard verbs or resources**
  - What to look for: `ClusterRole` or `Role` definitions with `verbs: ["*"]`, `resources: ["*"]`, or `apiGroups: ["*"]`.
  - Why it matters: Wildcard RBAC rules grant far more access than intended and violate least privilege. They can allow secret reading, pod exec, or privilege escalation.

### Secrets

- [ ] **Secrets containing credentials stored as plain Kubernetes Secrets without encryption at rest**
  - What to look for: `Secret` resources containing database passwords, API keys, or certificates in clusters where etcd encryption at rest is not configured (check `EncryptionConfiguration`).
  - Why it matters: Kubernetes Secrets are base64-encoded, not encrypted. Without etcd encryption at rest, anyone with etcd access or etcd backup access can read all secrets in plaintext.

---

## High Severity

These findings represent significant security gaps that could enable lateral movement, data exfiltration, or privilege escalation.

### Pod Security

- [ ] **ALL capabilities not dropped**
  - What to look for: Container specs missing `securityContext.capabilities.drop: ["ALL"]`. Even if specific capabilities are added, all should be dropped first.
  - Why it matters: Linux capabilities like `NET_RAW`, `SYS_PTRACE`, and `NET_ADMIN` enable network attacks, process debugging, and network reconfiguration. Dropping all and adding back only what is needed follows least privilege.

- [ ] **Writable root filesystem**
  - What to look for: Container specs missing `securityContext.readOnlyRootFilesystem: true`.
  - Why it matters: A writable root filesystem allows attackers to modify application binaries, install tools, or write web shells after initial compromise.

- [ ] **Privilege escalation not explicitly blocked**
  - What to look for: Container specs missing `securityContext.allowPrivilegeEscalation: false`.
  - Why it matters: When allowed, processes inside the container can gain more privileges than the parent process (e.g., via setuid binaries), potentially enabling container escape.

### Network Policies

- [ ] **No NetworkPolicy defined for the namespace (default allow-all)**
  - What to look for: Namespaces without any `NetworkPolicy` resources. Kubernetes default behavior is to allow all ingress and egress traffic between all pods.
  - Why it matters: Without network policies, any compromised pod can communicate with every other pod in the cluster, enabling lateral movement and access to internal services like databases.

- [ ] **Overly broad NetworkPolicy allowing all egress**
  - What to look for: NetworkPolicy resources with `egress: [{}]` or no egress restrictions, allowing pods to reach any destination including the internet, metadata services, and internal services.
  - Why it matters: Unrestricted egress enables data exfiltration, communication with command-and-control servers, and access to cloud metadata endpoints (169.254.169.254).

- [ ] **No explicit deny-all baseline policy**
  - What to look for: Namespaces missing a default-deny NetworkPolicy for both ingress and egress before more permissive policies are layered on.
  - Why it matters: A deny-all baseline ensures that new workloads are isolated by default and must have explicit network access granted, preventing accidental exposure.

### Secrets

- [ ] **Secrets passed as environment variables instead of mounted volumes**
  - What to look for: Pod specs using `env.valueFrom.secretKeyRef` to inject secrets as environment variables rather than mounting them as files via `volumes` and `volumeMounts`.
  - Why it matters: Environment variables are more easily leaked through process listings (`/proc/*/environ`), crash dumps, logging frameworks, and child process inheritance.

- [ ] **Service account tokens auto-mounted when not needed**
  - What to look for: Pod specs or ServiceAccount definitions without `automountServiceAccountToken: false` on workloads that do not interact with the Kubernetes API.
  - Why it matters: Auto-mounted tokens give every pod the ability to authenticate to the Kubernetes API. If the pod is compromised, the attacker inherits the service account's RBAC permissions.

### Image Security

- [ ] **Images using the `latest` tag or no tag**
  - What to look for: Container `image` fields ending in `:latest` or with no tag at all (e.g., `nginx` instead of `nginx:1.25.3`).
  - Why it matters: Mutable tags can point to different images over time, making it impossible to audit what code is running and enabling supply chain attacks through tag overwriting.

- [ ] **Images pulled from untrusted or public registries without verification**
  - What to look for: Image references pointing to Docker Hub, Quay, or other public registries without digest pinning (e.g., `@sha256:...`) and without image signature verification through admission controllers.
  - Why it matters: Public registry images can be modified or replaced by the publisher at any time. Digest pinning ensures immutability; signature verification ensures provenance.

### RBAC

- [ ] **Roles granting access to exec into pods or access pod logs across namespaces**
  - What to look for: `ClusterRole` resources granting `pods/exec`, `pods/attach`, or `pods/log` on all namespaces.
  - Why it matters: Pod exec is equivalent to SSH access to a container. Broad exec access enables reading secrets, application data, and lateral movement across the cluster.

- [ ] **Default service account used by application workloads**
  - What to look for: Deployments, StatefulSets, or Jobs that do not set `serviceAccountName` and therefore use the namespace `default` service account.
  - Why it matters: The default service account may accumulate permissions over time. Dedicated service accounts per workload enable fine-grained RBAC and reduce blast radius.

---

## Medium Severity

These findings represent defense-in-depth gaps that weaken overall cluster security posture.

### Pod Security

- [ ] **No Pod Security Standards (PSS) or Pod Security Admission (PSA) configured**
  - What to look for: Namespaces without `pod-security.kubernetes.io/enforce`, `pod-security.kubernetes.io/audit`, or `pod-security.kubernetes.io/warn` labels.
  - Why it matters: Without PSA enforcement, there is no cluster-level control preventing deployment of privileged, host-access, or root containers, relying entirely on manual review.

- [ ] **Containers with added capabilities beyond minimum required**
  - What to look for: `securityContext.capabilities.add` lists containing capabilities like `SYS_ADMIN`, `NET_RAW`, `SYS_PTRACE`, or `NET_ADMIN` without documented justification.
  - Why it matters: Each added capability expands the container's kernel attack surface. `SYS_ADMIN` in particular grants near-host-level privileges.

### Resource Limits

- [ ] **No CPU or memory resource limits defined**
  - What to look for: Container specs missing `resources.limits.cpu` and `resources.limits.memory`.
  - Why it matters: Without limits, a compromised or runaway container can consume all node resources, causing denial of service to co-located workloads (noisy neighbor / resource exhaustion attacks).

- [ ] **No resource requests defined**
  - What to look for: Container specs missing `resources.requests.cpu` and `resources.requests.memory`.
  - Why it matters: Without requests, the scheduler cannot make informed placement decisions, and QoS class defaults to BestEffort, making pods the first to be evicted under pressure.

- [ ] **No LimitRange or ResourceQuota configured for the namespace**
  - What to look for: Namespaces without `LimitRange` or `ResourceQuota` resources.
  - Why it matters: Without namespace-level quotas, a single application or compromised workload can consume unbounded cluster resources, affecting all tenants.

### Admission Control

- [ ] **No admission controller or OPA/Gatekeeper/Kyverno policies enforcing security baselines**
  - What to look for: Cluster without validating admission webhooks, OPA Gatekeeper `ConstraintTemplate` resources, or Kyverno `ClusterPolicy` resources.
  - Why it matters: Without admission control, security policies are advisory only. Developers can deploy non-compliant workloads (privileged containers, public services) without any automated enforcement.

- [ ] **No image allowlisting policy**
  - What to look for: Missing admission policies that restrict container images to approved registries or require image digest references.
  - Why it matters: Without image allowlisting, any user with deployment access can run arbitrary images from any registry, including images containing malware or backdoors.

### Network Policies

- [ ] **Access to cloud metadata endpoint (169.254.169.254) not blocked**
  - What to look for: Pods without egress NetworkPolicy blocking traffic to `169.254.169.254/32`, and no node-level iptables rules or metadata proxy configured.
  - Why it matters: The cloud metadata endpoint exposes instance credentials, user data scripts (often containing secrets), and infrastructure configuration. SSRF and compromised pods commonly target this endpoint.

### Secrets

- [ ] **No external secrets management integration**
  - What to look for: Secrets created as static `Secret` manifests rather than managed by External Secrets Operator, Sealed Secrets, Vault CSI driver, or a similar integration.
  - Why it matters: Static Kubernetes secrets require manual rotation, have no audit trail, and their plaintext values are stored in manifests that may be committed to version control.

---

## Low Severity

These findings represent best-practice improvements and operational hardening.

### Pod Security

- [ ] **No seccomp profile configured**
  - What to look for: Pod specs without `securityContext.seccompProfile.type: RuntimeDefault` or a custom seccomp profile.
  - Why it matters: Seccomp restricts which system calls a container can make, reducing the kernel attack surface. RuntimeDefault blocks commonly exploited syscalls with minimal application impact.

- [ ] **No AppArmor or SELinux profile applied**
  - What to look for: Pods without `apparmor.security.beta.kubernetes.io` annotations or `securityContext.seLinuxOptions` configured, on clusters where these LSMs are available.
  - Why it matters: MAC (Mandatory Access Control) profiles provide an additional layer of isolation beyond standard container boundaries, limiting file access and operations even if other controls are bypassed.

### Resource Limits

- [ ] **Missing pod disruption budgets for critical workloads**
  - What to look for: Deployments or StatefulSets with replicas greater than 1 without corresponding `PodDisruptionBudget` resources.
  - Why it matters: Without PDBs, node drains during upgrades or maintenance can take down all replicas simultaneously, causing availability loss for critical services.

### Operational Security

- [ ] **No liveness or readiness probes configured**
  - What to look for: Container specs without `livenessProbe` and `readinessProbe` definitions.
  - Why it matters: Without probes, Kubernetes cannot detect hung or crashed containers, leaving compromised or non-functional pods in the serving path indefinitely.

- [ ] **Labels and annotations missing for workload identification**
  - What to look for: Pods, Deployments, and Services without standard labels like `app.kubernetes.io/name`, `app.kubernetes.io/version`, and `app.kubernetes.io/managed-by`.
  - Why it matters: Consistent labeling enables effective network policies (label-based selectors), monitoring, and incident response by quickly identifying workload ownership and purpose.

- [ ] **No pod anti-affinity rules for high-availability workloads**
  - What to look for: Deployments with multiple replicas without `podAntiAffinity` rules to spread pods across nodes or availability zones.
  - Why it matters: Without anti-affinity, all replicas may land on the same node. A single node failure or compromise then affects all replicas simultaneously.

- [ ] **Namespace isolation not enforced**
  - What to look for: Multiple teams or applications sharing namespaces, or sensitive workloads deployed alongside non-sensitive workloads in the same namespace.
  - Why it matters: Namespace boundaries enable RBAC scoping, NetworkPolicy isolation, and resource quotas. Shared namespaces weaken these controls and increase blast radius.
