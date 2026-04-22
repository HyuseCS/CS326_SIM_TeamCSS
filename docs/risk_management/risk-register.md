# Risk Register

> **Project:** Deezcord 
> **Last Updated:** 2026-04-17  
> **Scoring:** Score = Likelihood × Impact (max 25)  
> 🔴 Critical = 15–25 &nbsp;|&nbsp; 🟡 Moderate = 8–14 &nbsp;|&nbsp; 🟢 Low = 1–7

---

## Risk Matrix

| #    | Risk | Likelihood (1–5) | Impact (1–5) | Score | Severity | Mitigation | Owner |
|------|------|:-:|:-:|:-:|:-:|---|---|
| R-01 | **WebSocket server crash under concurrent load** — Persistent socket connections mean a crash drops all active users simultaneously. | 4 | 5 | **20** | 🔴 Critical | Integrate a Redis pub/sub adapter (Socket.IO + Redis) to distribute connections. Add auto-restart via PM2 or Docker. Load-test with ≥ 100 concurrent users before release. | Theodore Pagalan |
| R-02 | **Sprint 1 scope overrun** — Six stories including real-time messaging in 2 weeks is aggressive; the WebSocket spike may consume more time than estimated. | 4 | 4 | **16** | 🔴 Critical | Front-load the WebSocket spike on Day 1. If it exceeds 2 days, defer US-06 to Sprint 2. PM to re-assess at the Apr 25 mid-sprint check-in. | Dominic Rejas |
| R-03 | **CI/CD pipeline misconfiguration delays deployment** — A broken pipeline close to the May 15 deadline could block the release. | 3 | 4 | **12** | 🟡 Moderate | Set up and validate the full pipeline by end of Week 1. Run a dry-run production deployment at end of Sprint 2 (May 9). | CJ Legaspi |
| R-04 | **Message delivery latency exceeds 500ms SLA** — Network conditions or an under-resourced server may cause noticeable chat lag. | 3 | 4 | **12** | 🟡 Moderate | Profile WebSocket broadcast paths early. Keep message payloads lightweight. Alert if staging p95 latency > 400ms. | Kent Butaya |
| R-05 | **Security vulnerability in auth flow** — Weak session handling or missing sanitization could expose credentials or enable XSS/CSRF attacks. | 2 | 5 | **10** | 🟡 Moderate | Use bcrypt (cost ≥ 12). Store JWTs in HttpOnly cookies. Sanitize all message content server-side. Conduct a security review in Week 4. | Kerby Fabria |
| R-06 | **Scope creep from new requirements** — Stakeholders may introduce features mid-project, threatening the May 15 date. | 3 | 3 | **9** | 🟡 Moderate | All new requirements must go through a formal CR. PM evaluates backlog and timeline impact. US-09/US-10 serve as scope buffer — new items displace them, not the deadline. | Theodore Pagalan |
| R-07 | **Team member unavailability** — A single absence on a 4-person team across 4 weeks measurably reduces sprint velocity. | 3 | 3 | **9** | 🟡 Moderate | Keep docs current so anyone can pick up any story. Cross-assign at least one reviewer per story. Identify droppable stories without breaking core functionality. | CJ Legaspi |
| R-08 | **Database grows unbounded with chat history** — High message volume could cause storage costs and query slowdowns. | 2 | 4 | **8** | 🟡 Moderate | Implement paginated history (50 per page) from Day 1. Index `(room_id, created_at)`. Set a soft cap of 10,000 messages per room. | Dominic Rejas |
| R-09 | **Browser compatibility issues with WebSockets** — Older browsers or restrictive firewalls may block socket connections. | 2 | 3 | **6** | 🟢 Low | Configure Socket.IO to fall back to HTTP long-polling. Test on Chrome, Firefox, Safari, and Edge before release. | Kent Butaya |
| R-10 | **Third-party email service outage** — Registration relies on an external mail provider; an outage blocks new user onboarding. | 2 | 3 | **6** | 🟢 Low | Add a secondary provider as fallback (e.g., AWS SES). Implement a "Resend Verification" button. Log all email failures with an alert. | Kerby Fabria |

---

## Risk Summary

| Severity     | Count | Risk IDs                               |
|--------------|:-----:|----------------------------------------|
| 🔴 Critical  | 2     | R-01, R-02                             |
| 🟡 Moderate  | 7     | R-03, R-04, R-05, R-06, R-07, R-08 |
| 🟢 Low       | 2     | R-09, R-10                             |

---
