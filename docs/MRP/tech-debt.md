# Technical Debt Register

**Project:** TeamCSS – Real-time Chat Application
**Version:** v0.8
**Team:** Butaya, Kent Vincent | Fabria, Kerby | Legaspi, Christian John | Rejas, Carl Dominic | Pagalan, Theodore
**Last Updated:** April 2026

---

## Overview

Technical debt refers to code-level shortcuts or incomplete implementations that work now but need to be revisited. This register tracks known debt in the TeamCSS project to ensure it is addressed in future sprints.

---

## Debt Items

### TD-01 — Hardcoded Configuration Values

| Field | Detail |
|---|---|
| **Area** | Backend |
| **Impact** | High |
| **Story Points** | 2 |
| **Status** | Open |
| **Assigned Sprint** | Sprint 3 |

**Problem:** Server port, database URL, and socket origin are hardcoded directly in `server.js` instead of using environment variables. This makes the app unsafe to share publicly and difficult to deploy across environments.

**Fix:** Extract all config values into a `.env` file and reference them using `process.env.VARIABLE_NAME`.

---

### TD-02 — No Input Validation on Chat Messages

| Field | Detail |
|---|---|
| **Area** | Frontend / Backend |
| **Impact** | High |
| **Story Points** | 3 |
| **Status** | Open |
| **Assigned Sprint** | Sprint 3 |

**Problem:** The message input has no validation — users can send empty messages, extremely long strings, or input containing scripts. This risks both poor UX and XSS vulnerabilities.

**Fix:** Add client-side checks (min/max length) and sanitize input server-side using `validator.js` or `DOMPurify` before storing or broadcasting.

---

### TD-03 — Socket Event Listeners Not Cleaned Up

| Field | Detail |
|---|---|
| **Area** | Frontend / WebSocket |
| **Impact** | Medium |
| **Story Points** | 2 |
| **Status** | ✅ Resolved in v0.8 |
| **Assigned Sprint** | Sprint 2 |

**Problem:** `socket.on('message')` listeners were added on component load but never removed when the user left a room. Over time this caused duplicate messages and JS heap memory to grow continuously.

**Fix:** Added `socket.off('message')` cleanup in the `useEffect` return. Memory leak confirmed resolved — see `performance.md` for before/after data.

---

### TD-04 — Missing Error Handling on API Calls

| Field | Detail |
|---|---|
| **Area** | Frontend / API Layer |
| **Impact** | Medium |
| **Story Points** | 3 |
| **Status** | ⚠️ Partially Resolved in v0.8 |
| **Assigned Sprint** | Sprint 2–3 |

**Problem:** Most fetch calls to the backend had no `try/catch`. If the server was unavailable, the UI would silently break with no feedback to the user.

**Fix:** Wrapped core API calls (`login`, `sendMessage`, `fetchHistory`) in `try/catch` blocks. Error messages now display in the UI. Remaining endpoints to be covered in Sprint 3.

---

### TD-05 — No Pagination for Chat History

| Field | Detail |
|---|---|
| **Area** | Backend / Frontend |
| **Impact** | Medium |
| **Story Points** | 5 |
| **Status** | Open |
| **Assigned Sprint** | Sprint 3 |

**Problem:** `GET /api/messages` returns all messages at once regardless of count. As rooms grow, this causes slow load times, high memory use, and poor mobile performance.

**Fix:** Implement limit/offset or cursor-based pagination — load the last 50 messages by default, then fetch older ones as the user scrolls up.

---

## Summary

| ID | Description | Impact | Points | Status |
|---|---|---|---|---|
| TD-01 | Hardcoded config values | High | 2 | Open |
| TD-02 | No input validation | High | 3 | Open |
| TD-03 | Uncleaned socket listeners | Medium | 2 | ✅ Resolved |
| TD-04 | Missing API error handling | Medium | 3 | ⚠️ Partial |
| TD-05 | No chat history pagination | Medium | 5 | Open |

**Total Debt:** 15 story points &nbsp;|&nbsp; **Resolved:** 2 pts &nbsp;|&nbsp; **Remaining:** 13 pts
