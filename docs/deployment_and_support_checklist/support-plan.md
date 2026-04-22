# Support Plan

**Project:** Deezcord  
**Effective Date:** May 15, 2026 (Post-Launch)

---

## 1. Support Team and Contact Matrix
        During the initial post-launch phase, the following team members will handle support escalations based on their Sprint 2 / Release roles:

- **Infrastructure & Uptime (DevOps Leads):** 
        Dominic Rejas (rejas.dominic@gmail.com), Kent Butaya (butaya.kentvincent07@gmail.com)
- **Bug Triaging & Testing (QA Lead):** 
        Theodore Pagalan (pagalan.theodoreustp@gmail.com)
- **User Documentation & Runbooks (Docs Lead):** 
        Kerby Fabria (kerbyfabriabual@gmail.com)
- **Stakeholder Communication (PM):** 
        Christian John Legaspi (christianjohn.legaspi@1.ustp.edu.ph)

## 2. Issue Reporting Process
Users and stakeholders can report issues through the following channels:
1. **In-App Feedback:** 
        Users can click the "Report an Issue" button inside any chat room to submit a bug report directly to our issue tracker.
2. **Email Support:** 
        Critical issues or account-related inquiries can be sent to **[EMAIL_ADDRESS]** (to be determined).
3. **GitHub Issues (Internal):** 
        The QA lead and DevOps leads will triage and log all verified bugs as GitHub Issues for sprint tracking.

## 3. Response Times & SLAs
We are committed to addressing reported issues based on their severity:
- **Severity 1 (Critical):** System down, complete WebSocket failure, or major security vulnerability.
  - **Response Time:** < 2 hours
  - **Resolution Target:** < 12 hours
- **Severity 2 (High):** Core feature broken (e.g., cannot create rooms or send messages), but a workaround exists.
  - **Response Time:** < 8 hours
  - **Resolution Target:** < 24 hours
- **Severity 3 (Medium):** Minor bug, UI glitch, or isolated profile avatar issue.
  - **Response Time:** < 24 hours
  - **Resolution Target:** Addressed in the next sprint
- **Severity 4 (Low):** Feature requests or minor enhancements.
  - **Response Time:** < 48 hours
  - **Resolution Target:** Added to product backlog

## 4. Scope of Support
The team will provide support for the following core functionalities:
- **Account Access:** Registration issues, login failures, and session persistence.
- **Room Management:** Issues with creating, joining, leaving, and deleting chat rooms, as well as invite codes for private rooms.
- **Real-Time Chat:** Addressing WebSocket latency (> 500ms), missed messages, auto-scrolling issues, and connection drops.
- **Moderation:** Handling false positives in the automated profanity filter and addressing issues with manual admin message deletion.

## 5. Monitoring and Maintenance
- **System Monitoring:** The DevOps Leads will monitor the CI/CD pipeline, WebSocket server stability, and the Redis pub/sub instances.
- **Error Logging:** Client-side and server-side errors (e.g., failed WebSocket connections, DB timeouts) will be actively logged and monitored for unusual spikes.
- **Routine Maintenance:** Any scheduled downtime will be communicated to users in advance via system messages within the chat rooms.

## 6. Issue Escalation Workflow
1. **Tier 1 (Triage & Documentation):**
   - Review incoming user issues. Check against the single source of truth in the `/docs` folder, User Guide, and API documentation (managed by Docs Lead).
2. **Tier 2 (Bug Verification):**
   - The QA Lead verifies reproducible bugs, logs them into the issue tracker, and determines severity.
3. **Tier 3 (Technical Resolution):**
   - Critical infrastructure, database, or server issues are escalated to the DevOps Leads for immediate patching, reconfiguration, or server restarts.

## 7. Known Issues and Limitations
- **Latency Under Load:** WebSocket reconnections might experience a slight delay under heavy load. The system is designed to auto-reconnect and fetch missed messages (up to 50 historical messages per load limit).
- **Profanity Filter:** The filter relies on a server-side word list. False positives or missed inappropriate words should be reported. Room admins maintain manual deletion rights as a fallback.
