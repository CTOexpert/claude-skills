# API Security Review

This checklist covers security review of API implementations and configurations across REST APIs, GraphQL, gRPC, and WebSocket endpoints. Use it to evaluate authentication, authorization, input validation, data exposure, and transport security in API code, gateway configurations, and specification files (OpenAPI, GraphQL schemas, protobuf definitions).

---

## Critical Severity

These findings represent immediate, exploitable risks that could lead to data breach, unauthorized access, or system compromise.

### Authentication

- [ ] **No authentication on sensitive endpoints**
  - What to look for: API routes or resolvers that access, modify, or delete user data, administrative functions, or internal operations without requiring any authentication token, session, or API key. Check middleware/filter chains, route definitions, and decorator annotations.
  - Why it matters: Unauthenticated endpoints are directly accessible to anyone who discovers the URL. This is the most common and impactful API vulnerability (OWASP API1: Broken Object Level Authorization).

- [ ] **Authentication bypass through parameter manipulation**
  - What to look for: Endpoints that accept user identifiers (user ID, email, account number) as request parameters and use those values to determine access without verifying them against the authenticated session's identity.
  - Why it matters: An attacker can change the identifier parameter to access another user's data, even when properly authenticated. This is a Broken Object Level Authorization (BOLA/IDOR) vulnerability.

- [ ] **JWT tokens without signature verification or using `alg: none`**
  - What to look for: JWT validation code that does not verify the signature, accepts the `none` algorithm, or allows the client to specify the signing algorithm via the `alg` header without server-side enforcement.
  - Why it matters: Without proper signature verification, attackers can forge valid-looking tokens with arbitrary claims, gaining access as any user or role.

### Injection

- [ ] **SQL injection vectors in database queries**
  - What to look for: String concatenation or template literals used to construct SQL queries with user-supplied input, rather than parameterized queries or ORM methods. Check raw query calls, stored procedure invocations, and dynamic query builders.
  - Why it matters: SQL injection allows attackers to read, modify, or delete arbitrary database data, bypass authentication, and potentially execute system commands on the database server.

- [ ] **Command injection through unsanitized input passed to system calls**
  - What to look for: User input passed to `os.system()`, `subprocess.run()` with `shell=True`, `exec()`, `eval()`, backtick execution, or similar functions that interpret strings as commands.
  - Why it matters: Command injection gives attackers direct operating system access, enabling data exfiltration, backdoor installation, and lateral movement to other systems.

- [ ] **Server-Side Request Forgery (SSRF) through user-controlled URLs**
  - What to look for: API endpoints that accept URLs as input and make server-side HTTP requests to those URLs (webhooks, URL preview, file import, proxy endpoints) without validating or restricting the target.
  - Why it matters: SSRF allows attackers to access internal services, cloud metadata endpoints (169.254.169.254), and private network resources through the server, bypassing network firewalls.

- [ ] **GraphQL injection or unrestricted introspection in production**
  - What to look for: GraphQL endpoints with introspection enabled in production, no query depth limits, no query complexity analysis, or resolvers that construct database queries from user-supplied arguments without parameterization.
  - Why it matters: Introspection reveals the entire API schema to attackers. Unrestricted queries enable denial-of-service through deeply nested or expensive queries, and resolver injection exposes backend data.

---

## High Severity

These findings represent significant security gaps that could enable data exposure, account takeover, or service disruption.

### Authorization

- [ ] **Missing function-level access control**
  - What to look for: Administrative endpoints (user management, configuration, reports) accessible to regular user roles. Check that role-based or permission-based authorization is enforced at each endpoint, not just at the application perimeter.
  - Why it matters: Without per-endpoint authorization, any authenticated user can access administrative functions, enabling privilege escalation and unauthorized data access.

- [ ] **Inconsistent authorization between REST endpoints and GraphQL resolvers**
  - What to look for: APIs that expose the same data through multiple interfaces (REST and GraphQL, or REST and gRPC) with authorization logic only applied to one interface.
  - Why it matters: Attackers will probe all available interfaces. If authorization is enforced on the REST API but not the GraphQL endpoint, the GraphQL endpoint becomes a bypass path.

- [ ] **Mass assignment or excessive data binding**
  - What to look for: Endpoints that bind request body fields directly to database models or internal objects without an explicit allowlist of permitted fields. In particular, check for user-modifiable fields like `role`, `isAdmin`, `accountBalance`, or `permissions`.
  - Why it matters: Attackers can add unexpected fields to requests to modify protected attributes, escalating privileges or manipulating data beyond their authorized scope.

### Rate Limiting

- [ ] **No rate limiting or throttling on authentication endpoints**
  - What to look for: Login, password reset, OTP verification, and token exchange endpoints without rate limiting, account lockout, or progressive delays.
  - Why it matters: Without rate limiting, attackers can perform unlimited brute-force attempts against credentials, OTPs, and password reset tokens, eventually gaining unauthorized access.

- [ ] **No rate limiting on resource-intensive operations**
  - What to look for: Endpoints that trigger expensive operations (report generation, file processing, search queries, bulk exports) without per-user or per-IP rate limits.
  - Why it matters: Unrestricted access to expensive operations enables denial-of-service attacks that exhaust server resources, database connections, or downstream service capacity.

### Error Handling

- [ ] **Verbose error messages exposing internal details**
  - What to look for: API error responses that include stack traces, database query text, internal file paths, server software versions, or internal IP addresses. Check both application-level errors and framework default error handlers.
  - Why it matters: Detailed error messages provide attackers with reconnaissance information about the technology stack, database schema, file structure, and internal network topology.

- [ ] **Different error responses revealing existence of resources or users**
  - What to look for: Login endpoints returning "invalid password" vs "user not found", or resource endpoints returning 404 for non-existent items but 403 for unauthorized items, allowing user/resource enumeration.
  - Why it matters: Differential error responses allow attackers to enumerate valid usernames, email addresses, or resource IDs, which are then used in targeted attacks.

### Data Exposure

- [ ] **Sensitive fields returned in API responses without need**
  - What to look for: User objects returning password hashes, tokens, internal IDs, or PII fields that the client does not use. Check serializers, response schemas, and GraphQL type definitions for over-exposed fields.
  - Why it matters: Excessive data exposure violates the principle of least privilege and increases the impact of any API compromise or man-in-the-middle attack.

- [ ] **No pagination on list endpoints returning large datasets**
  - What to look for: Endpoints that return all matching records without enforcing maximum page size, default limits, or cursor-based pagination.
  - Why it matters: Unlimited list responses enable data harvesting (scraping all records) and denial-of-service through memory exhaustion on the server.

### Transport Security

- [ ] **API accessible over HTTP without TLS redirect**
  - What to look for: API endpoints responding on port 80 without redirecting to HTTPS, or TLS termination configured but HTTP access not blocked at the load balancer or gateway level.
  - Why it matters: API traffic over HTTP is transmitted in plaintext, exposing authentication tokens, request/response bodies, and PII to network eavesdropping.

- [ ] **Weak TLS configuration (TLS 1.0/1.1 or weak cipher suites)**
  - What to look for: Server or load balancer TLS configuration allowing TLS 1.0, TLS 1.1, or weak cipher suites (RC4, DES, 3DES, export ciphers, NULL ciphers).
  - Why it matters: Older TLS versions and weak cipher suites have known vulnerabilities (POODLE, BEAST, SWEET32) that allow decryption of intercepted traffic.

---

## Medium Severity

These findings represent defense-in-depth gaps that weaken the overall API security posture.

### Input Validation

- [ ] **No request size limits**
  - What to look for: Missing `Content-Length` limits, maximum request body size configuration, or file upload size restrictions on the API gateway, web server, or application framework.
  - Why it matters: Unlimited request sizes enable denial-of-service through memory exhaustion and can be used to bypass WAF rules that only inspect a limited portion of the request body.

- [ ] **No input schema validation against OpenAPI/GraphQL schema**
  - What to look for: Endpoints that process request bodies without validating against a defined schema, accepting unexpected fields, wrong types, or missing required fields silently.
  - Why it matters: Without schema validation, the API may process malformed input in unexpected ways, leading to type confusion bugs, injection attacks, or business logic bypasses.

- [ ] **Missing Content-Type validation**
  - What to look for: Endpoints that process request bodies without verifying the `Content-Type` header matches the expected format (e.g., accepting `application/xml` when only `application/json` is intended).
  - Why it matters: Content-Type confusion can lead to XML External Entity (XXE) attacks, deserialization vulnerabilities, or bypasses of input validation that only handles the expected format.

- [ ] **No output encoding for user-generated content**
  - What to look for: API responses that include user-supplied content without encoding, particularly in HTML-rendered contexts, email templates, or PDF generation.
  - Why it matters: Missing output encoding enables Cross-Site Scripting (XSS) when API responses are rendered in browsers, and injection in other output contexts (email, PDF).

### Authentication

- [ ] **Long-lived access tokens without refresh mechanism**
  - What to look for: JWT or opaque access tokens with expiration times exceeding 15-30 minutes, without a refresh token flow for obtaining new short-lived tokens.
  - Why it matters: Long-lived tokens increase the window of opportunity if a token is compromised. Short-lived tokens with refresh reduce exposure while maintaining user experience.

- [ ] **No token revocation mechanism**
  - What to look for: Authentication systems using stateless JWTs without a server-side revocation list, blocklist, or short expiration paired with refresh tokens that can be individually revoked.
  - Why it matters: Without revocation, compromised tokens remain valid until expiration. Password changes, account deactivation, or suspicious activity detection cannot immediately invalidate existing sessions.

- [ ] **API keys used as sole authentication without additional controls**
  - What to look for: Endpoints authenticated only by API key in query parameters or headers, without additional controls like IP allowlisting, mutual TLS, or request signing.
  - Why it matters: API keys are static, shared secrets that are easily leaked through logs, browser history (if in URLs), or client-side code. They should be layered with additional authentication factors.

### Data Exposure

- [ ] **Missing CORS configuration review**
  - What to look for: CORS headers allowing `Access-Control-Allow-Origin: *` on authenticated endpoints, or reflecting the `Origin` header without validation, or allowing credentials with wildcard origins.
  - Why it matters: Misconfigured CORS allows malicious websites to make authenticated cross-origin requests, potentially exfiltrating user data through the victim's browser session.

- [ ] **No field-level authorization on response data**
  - What to look for: Endpoints that return the same response fields regardless of the requester's role or permissions, rather than filtering sensitive fields based on authorization level.
  - Why it matters: An endpoint may correctly require authentication but still expose admin-level fields (internal notes, audit data, financial details) to regular users in the response body.

- [ ] **Sensitive data in URL query parameters**
  - What to look for: Tokens, passwords, PII, or API keys passed as URL query parameters rather than in request headers or body.
  - Why it matters: URL parameters are logged by web servers, proxy servers, browsers, and CDNs. Sensitive data in URLs is widely exposed in access logs and referrer headers.

### Logging

- [ ] **No request/response logging for security-relevant endpoints**
  - What to look for: Missing structured logging for authentication attempts, authorization failures, input validation errors, and administrative operations.
  - Why it matters: Without logging, security incidents cannot be detected, investigated, or correlated. Audit trails are essential for incident response and compliance.

- [ ] **Sensitive data logged in API request/response logs**
  - What to look for: Log entries containing plaintext passwords, tokens, credit card numbers, SSNs, or other sensitive fields from request bodies or response payloads.
  - Why it matters: Logs are often stored with less access control than application databases. Sensitive data in logs expands the attack surface and may violate data protection regulations (GDPR, PCI-DSS).

---

## Low Severity

These findings represent best-practice improvements and hardening recommendations.

### Transport Security

- [ ] **Missing security headers (HSTS, X-Content-Type-Options, X-Frame-Options)**
  - What to look for: API responses without `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, `X-Frame-Options`, or `Content-Security-Policy` headers.
  - Why it matters: Security headers provide defense-in-depth against protocol downgrade attacks, MIME type confusion, clickjacking, and content injection, particularly for APIs consumed by browsers.

### API Design

- [ ] **No API versioning strategy**
  - What to look for: APIs without version indicators in the URL path (`/v1/`), headers (`Accept: application/vnd.api.v1+json`), or query parameters.
  - Why it matters: Without versioning, security fixes that change API behavior (input validation, field removal) must be deployed as breaking changes, slowing security remediation.

- [ ] **No deprecation policy for old API versions**
  - What to look for: Multiple API versions running simultaneously without documented sunset dates, deprecation warnings in responses, or plans to retire insecure older versions.
  - Why it matters: Old API versions may lack security controls added to newer versions. Without a deprecation timeline, insecure endpoints remain accessible indefinitely.

- [ ] **No OpenAPI/Swagger specification maintained for the API**
  - What to look for: APIs without an up-to-date machine-readable specification (OpenAPI, GraphQL SDL, or protobuf definitions) that documents all endpoints, parameters, and response schemas.
  - Why it matters: Without a specification, security reviews are ad-hoc and incomplete. Specifications enable automated security testing, input validation, and documentation generation.

### WebSocket Security

- [ ] **WebSocket connections without origin validation**
  - What to look for: WebSocket upgrade handlers that accept connections from any origin without checking the `Origin` header against an allowlist.
  - Why it matters: Without origin validation, a malicious website can establish a cross-origin WebSocket connection using the victim's browser credentials, enabling cross-site WebSocket hijacking.

- [ ] **No message size or rate limits on WebSocket frames**
  - What to look for: WebSocket handlers that accept messages of arbitrary size and frequency without per-connection limits.
  - Why it matters: Unlimited message sizes can exhaust server memory, and unlimited message rates can overwhelm server processing capacity, enabling denial-of-service attacks.

### gRPC Security

- [ ] **gRPC reflection service enabled in production**
  - What to look for: gRPC servers with the reflection service (`grpc.reflection.v1alpha.ServerReflection`) registered in production deployments.
  - Why it matters: The reflection service exposes the full protobuf schema and available methods to any client, providing attackers with a complete map of the API surface without requiring documentation access.

- [ ] **No deadline/timeout configuration on gRPC calls**
  - What to look for: gRPC client and server configurations without default deadlines, or server handlers without timeout enforcement.
  - Why it matters: Without deadlines, slow or hung requests consume server resources indefinitely. Propagating deadlines through service chains prevents cascading resource exhaustion.
