# Performance Report

**Project:** TeamCSS – Real-time Chat Application
**Version:** v0.8 (Post-Refactor)
**Team:** Butaya, Kent Vincent | Fabria, Kerby | Legaspi, Christian John | Rejas, Carl Dominic | Pagalan, Theodore
**Date:** April 2026

---

## Overview

This document compares the TeamCSS application's performance **before** and **after** the refactoring changes in v0.8. The refactor focused on three areas: memory stability, page load speed, and code cleanliness.

---

## What Was Refactored

| # | Change | Files Affected | Linked Debt |
|---|---|---|---|
| 1 | Added socket listener cleanup on unmount | `ChatRoom.jsx` | TD-03 |
| 2 | Wrapped core API calls in `try/catch` | `api.js`, `AuthService.js` | TD-04 |
| 3 | Removed unused imports and dead code | Multiple files | — |
| 4 | Shortened long functions (>50 lines split up) | `chatController.js` | — |
| 5 | Moved magic numbers to named constants | `socket.js`, `config.js` | TD-01 |

---

## Before vs. After Comparison

### Page Load Time

| Metric | Before | After | Change |
|---|---|---|---|
| Initial load time | ~3.2s | ~2.1s | ✅ −34% |
| DOM content loaded | ~1.8s | ~1.2s | ✅ −33% |
| Time to interactive | ~4.0s | ~2.5s | ✅ −37.5% |

> Measured using Chrome DevTools → Performance tab. Average of 3 runs on simulated Fast 3G.

---

### Memory Usage (After 10 Minutes of Active Use)

| Metric | Before | After | Change |
|---|---|---|---|
| JS Heap Size | ~85 MB | ~52 MB | ✅ −39% |
| Active Socket Listeners | 12+ (growing) | 4 (stable) | ✅ Leak fixed |
| Detached DOM Nodes | 8 | 0 | ✅ Cleaned up |

> The primary gain here was fixing TD-03. The heap no longer grows over time — it stays flat during extended use.

---

### API Response Time

| Endpoint | Before | After | Change |
|---|---|---|---|
| `POST /api/login` | 420ms | 390ms | ✅ −7% |
| `GET /api/messages` | 850ms | 780ms | ✅ −8% |
| `POST /api/messages` | 310ms | 290ms | ✅ −6% |

> Improvements are minor here as no backend logic was overhauled. Bigger gains expected once TD-05 (pagination) is implemented in Sprint 3.

---

### Code Quality

| Metric | Before | After |
|---|---|---|
| ESLint warnings | 18 | 3 |
| Files with unused imports | 11 | 0 |
| Functions over 50 lines | 7 | 2 |
| Commented-out code blocks | 14 | 0 |

---

## Conclusion

The v0.8 refactor delivered meaningful improvements, especially in memory stability (−39% heap size) and page load time (up to −37.5%). The most impactful fix was resolving the socket listener memory leak (TD-03). Code quality metrics also improved significantly, making the codebase easier to maintain going forward.

Remaining open debt (TD-01, TD-02, TD-05) is logged in `tech-debt.md` and will be addressed in Sprint 3.

---

## Next Steps

- [ ] Implement message pagination — TD-05 (Sprint 3)
- [ ] Complete `.env` migration — TD-01 (Sprint 3)
- [ ] Add full input validation — TD-02 (Sprint 3)
- [ ] Run Lighthouse audit after Sprint 3 changes
