# Sprint 1 Plan

> **Project:** Deezcord
> **Sprint Duration:** Week 1 – Week 2 (April 21 – May 2, 2026)  
> **Sprint Goal:** Deliver a working authentication flow and the core room experience so that a user can register, log in, create a room, and exchange real-time messages end-to-end.  
> **Team Capacity:** ~13 story points (conservative; accounts for environment setup and WebSocket spike in Week 1)

---

## Selected Stories

| Story | Title                             | Points | Priority | Owner           |
|-------|-----------------------------------|--------|----------|-----------------|
| US-01 | User Registration                 | 2      | 🔴 High  | Theodore Pagalan       |
| US-02 | User Login & Logout               | 1      | 🔴 High  | CJ Legaspi       |
| US-03 | Create a Chat Room                | 2      | 🔴 High  | Kent Butaya       |
| US-04 | Browse and Join Public Rooms      | 3      | 🔴 High  | Kerby Fabria       |
| US-05 | Send & Receive Real-time Messages | 5      | 🔴 High  | Dominic Rejas |
| **Total** |                               | **13** |          |                 |



---

## Sprint Backlog Detail

### US-01 — User Registration
**Owner:** Theodore Pagalan  
**Tasks:**
- [ ] Design registration form UI (username, email, password, confirm password)
- [ ] Implement `POST /auth/register` endpoint with input validation
- [ ] Integrate email verification service (e.g., SendGrid)
- [ ] Write unit tests for registration logic

---

### US-02 — User Login & Logout
**Owner:** CJ Legaspi  
**Tasks:**
- [ ] Build login form UI with "Remember Me" toggle
- [ ] Implement JWT-based session management with secure cookie
- [ ] Add `POST /auth/logout` endpoint and disconnect active sockets on logout
- [ ] Handle invalid credential errors gracefully on the front end

---

### US-03 — Create a Chat Room
**Owner:** Kent Butaya  
**Tasks:**
- [ ] Design and build "New Room" modal (name, topic, public/private toggle)
- [ ] Implement `POST /rooms` API endpoint; generate invite code for private rooms
- [ ] Auto-assign creator as room admin in the database
- [ ] Push new room to the browser list via WebSocket broadcast

---

### US-04 — Browse and Join Public Rooms
**Owner:** Kerby Fabria  
**Tasks:**
- [ ] Build room browser UI with sort controls and live-filter search bar
- [ ] Implement `GET /rooms` endpoint returning public rooms with member count
- [ ] Handle "Join Room" action: authenticate, subscribe to room's WebSocket channel
- [ ] Show loading and empty states

---

### US-05 — Send & Receive Real-time Messages
**Owner:** Dominic Rejas  
**Tasks:**
- [ ] Spike: choose and configure WebSocket library (e.g., Socket.IO or native WS)
- [ ] Implement message emit/broadcast on the server; persist each message to DB
- [ ] Build chat input component with send-on-Enter support
- [ ] Implement auto-scroll behavior and reconnection logic with missed-message catch-up

---

