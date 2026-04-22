# Performance Analysis Report

**Project:** TeamCSS – Real-time Chat Application  
**Version:** v0.8 (Post-Refactor)  
**Team:** Butaya, Kent Vincent | Fabria, Kerby | Legaspi, Christian John | Rejas, Carl Dominic | Pagalan, Theodore  
**Date:** April 2026  

---

## Overview

This document compares the system's performance **before** and **after** the refactoring changes introduced in v0.8. Improvements were focused on reducing load times, cleaning up memory leaks, and improving code readability and maintainability.

---

## Refactoring Changes Made

| # | Change | File(s) Affected |
|---|--------|-----------------|
| 1 | Extracted hardcoded config to `.env` | `server.js`, `config.js` |
| 2 | Added input sanitization on message send | `chatController.js`, `MessageInput.jsx` |
| 3 | Added socket listener cleanup on unmount | `ChatRoom.jsx` |
| 4 | Added try/catch error handling on API calls | `api.js`, `AuthService.js` |
| 5 | Cleaned up unused imports and dead code | Multiple files |

---

## Performance Comparison

### 1. Page Load Time (Chat Room)

| Metric              | Before Refactor | After Refactor | Change     |
|---------------------|-----------------|----------------|------------|
| Initial load time   | ~3.2s           | ~2.1s          | ✅ −34%    |
| DOM content loaded  | ~1.8s           | ~1.2s          | ✅ −33%    |
| Time to interactive | ~4.0s           | ~2.5s          | ✅ −37.5%  |

> Measured using Chrome DevTools → Performance tab (3 runs averaged, simulated Fast 3G network)

---

### 2. Memory Usage (After 10 Minutes of Use)

| Metric              | Before Refactor | After Refactor | Change     |
|---------------------|-----------------|----------------|------------|
| JS Heap Size        | ~85 MB          | ~52 MB         | ✅ −39%    |
| Active Listeners    | 12+ (growing)   | 4 (stable)     | ✅ Fixed leak |
| Detached DOM nodes  | 8               | 0              | ✅ Cleaned |

> Memory leak from duplicate socket listeners (TD-03) was resolved. Heap no longer grows unboundedly.

---

### 3. API Response Time

| Endpoint              | Before  | After   | Change   |
|-----------------------|---------|---------|----------|
| `POST /api/login`     | 420ms   | 390ms   | ✅ −7%   |
| `GET /api/messages`   | 850ms   | 780ms   | ✅ −8%   |
| `POST /api/messages`  | 310ms   | 290ms   | ✅ −6%   |

> Minor improvements due to removal of redundant middleware calls and cleaner async handling.

---

### 4. Code Quality Metrics

| Metric                  | Before Refactor | After Refactor |
|-------------------------|-----------------|----------------|
| ESLint warnings         | 18              | 3              |
| Unused imports          | 11 files        | 0 files        |
| Functions > 50 lines    | 7               | 2              |
| Commented-out code      | 14 blocks       | 0 blocks       |

---

## Conclusion

The v0.8 refactor resulted in measurable improvements across load time, memory stability, and code maintainability. The most significant gains came from resolving the socket listener leak and cleaning up dead code. Remaining technical debt (TD-01, TD-02, TD-05) is documented in `tech-debt.md` and is scheduled for future sprints.

---

## Next Steps

- [ ] Implement message pagination (TD-05) in Sprint 3
- [ ] Add automated performance benchmarking (Lighthouse CI)
- [ ] Monitor memory usage in production via browser telemetry
