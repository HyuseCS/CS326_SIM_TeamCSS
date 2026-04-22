# Technical Debt Register

**Project:** TeamCSS – Real-time Chat Application  
**Version:** v0.8  
**Team:** Butaya, Kent Vincent | Fabria, Kerby | Legaspi, Christian John | Rejas, Carl Dominic | Pagalan, Theodore  

---

## What is Technical Debt?

Technical debt refers to shortcuts, workarounds, or suboptimal implementations made during development that will need to be fixed or improved in the future. Addressing tech debt improves code quality, maintainability, and performance.

---

## Technical Debt Items

### TD-01 · Hardcoded Configuration Values
**Area:** Backend / Config  
**Description:** Environment-specific values such as server ports, database URLs, and API keys are hardcoded directly in source files instead of being managed through environment variables (`.env`).  
**Impact:** High – Makes deployment to different environments error-prone and poses a security risk.  
**Proposed Fix:** Move all config values to a `.env` file and access them via `process.env` variables.  
**Effort Estimate:** 2 story points  

---

### TD-02 · No Input Validation on Chat Messages
**Area:** Frontend / Backend  
**Description:** Messages submitted through the chat form are not validated or sanitized before being stored or broadcast. This can allow empty messages, excessively long strings, or potentially malicious input.  
**Impact:** High – Risk of XSS attacks and degraded user experience.  
**Proposed Fix:** Add client-side length checks and server-side sanitization using a library such as `DOMPurify` or `validator.js`.  
**Effort Estimate:** 3 story points  

---

### TD-03 · Duplicate Event Listeners Not Cleaned Up
**Area:** Frontend / WebSocket  
**Description:** Socket.io event listeners (e.g., `on('message')`) are attached on component mount but are not removed when a component unmounts or the user navigates away, causing duplicate listener accumulation.  
**Impact:** Medium – Leads to memory leaks and duplicate message rendering over time.  
**Proposed Fix:** Implement cleanup logic (e.g., `socket.off('message')`) in component teardown or `useEffect` return functions.  
**Effort Estimate:** 2 story points  

---

### TD-04 · Lack of Error Handling for Failed API Calls
**Area:** Frontend / API Layer  
**Description:** Fetch/axios calls to the backend do not have consistent error handling. If a request fails (e.g., server is down), the UI does not show a meaningful error message to the user.  
**Impact:** Medium – Poor user experience; silent failures make debugging difficult.  
**Proposed Fix:** Wrap all API calls in `try/catch` blocks and display appropriate error toasts or messages in the UI.  
**Effort Estimate:** 3 story points  

---

### TD-05 · No Pagination for Chat History
**Area:** Backend / Frontend  
**Description:** The chat history feature (US-06) loads all messages from the database at once, with no limit or pagination. As the message count grows, this will cause performance degradation.  
**Impact:** Medium – Slow load times and high memory usage for rooms with many messages.  
**Proposed Fix:** Implement cursor-based or offset-based pagination (e.g., load last 50 messages, load more on scroll).  
**Effort Estimate:** 5 story points  

---

## Summary Table

| ID    | Description                          | Impact | Effort | Status      |
|-------|--------------------------------------|--------|--------|-------------|
| TD-01 | Hardcoded config values              | High   | 2 pts  | Open        |
| TD-02 | No input validation on messages      | High   | 3 pts  | Open        |
| TD-03 | Duplicate event listeners            | Medium | 2 pts  | Open        |
| TD-04 | No error handling for API calls      | Medium | 3 pts  | Open        |
| TD-05 | No pagination for chat history       | Medium | 5 pts  | Open        |

**Total Effort to Resolve:** 15 story points
