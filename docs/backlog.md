# Product Backlog

> **Project:** Real-time Chat Rooms – A web application for creating and joining topic-based live chat rooms  
> **Last Updated:** 2026-04-17

---

## User Stories

---

### US-01 — User Registration
**Priority:** 🔴 High | **Story Points:** 2

> *As a* **new user**, *I want to* **register an account with a username, email, and password** *so that* **I can access chat rooms and have a persistent identity in conversations.**

**Acceptance Criteria:**
- [ ] Registration form requires a unique username, valid email, and password (min. 8 characters).
- [ ] System rejects duplicate usernames or emails with a specific, friendly error message.
- [ ] A verification email is sent upon successful registration.
- [ ] After verification, the user is redirected to the room browser.

---

### US-02 — User Login & Logout
**Priority:** 🔴 High | **Story Points:** 1

> *As a* **registered user**, *I want to* **log in and log out securely** *so that* **my account and chat history are protected from unauthorized access.**

**Acceptance Criteria:**
- [ ] User can log in using their email/username and password.
- [ ] Failed login attempts show a generic error without revealing which field is incorrect.
- [ ] "Remember Me" option persists the session for up to 7 days via a secure cookie.
- [ ] Logout clears the session and disconnects any active WebSocket connections.

---

### US-03 — Create a Chat Room
**Priority:** 🔴 High | **Story Points:** 2

> *As a* **logged-in user**, *I want to* **create a new chat room with a name and topic** *so that* **I can host conversations around a subject I care about.**

**Acceptance Criteria:**
- [ ] Room creation form includes: Room Name (required, unique), Topic/Description, and Public/Private toggle.
- [ ] Private rooms require an invite code to join; public rooms appear in the room browser.
- [ ] Newly created rooms appear in the room list immediately without a page reload.
- [ ] The creator is automatically set as the room admin.

---

### US-04 — Browse and Join Public Rooms
**Priority:** 🔴 High | **Story Points:** 3

> *As a* **user**, *I want to* **browse a list of public chat rooms and join one with a click** *so that* **I can discover and participate in conversations that interest me.**

**Acceptance Criteria:**
- [ ] Room browser displays all public rooms with name, topic, member count, and live indicator.
- [ ] Rooms can be sorted by newest, most active, or alphabetical order.
- [ ] Joining a room immediately loads the chat interface and marks the user as online.
- [ ] A search bar filters rooms by name or topic keyword in real time.

---

### US-05 — Send and Receive Real-time Messages
**Priority:** 🔴 High | **Story Points:** 5

> *As a* **room member**, *I want to* **send messages and see others' messages appear instantly** *so that* **the conversation feels live and fluid without needing to refresh the page.**

**Acceptance Criteria:**
- [ ] Messages are delivered to all room members via WebSocket within 500ms under normal conditions.
- [ ] Each message displays the sender's username, avatar, and a timestamp.
- [ ] New messages auto-scroll to the bottom of the chat window unless the user has scrolled up.
- [ ] Disconnected users are automatically reconnected and shown missed messages on rejoin.

---

### US-06 — View Chat History
**Priority:** 🔴 High | **Story Points:** 3

> *As a* **room member**, *I want to* **scroll up to see previous messages when I join a room** *so that* **I have context for the ongoing conversation.**

**Acceptance Criteria:**
- [ ] On joining, the last 50 messages are loaded and displayed in the chat window.
- [ ] Scrolling to the top triggers lazy-loading of the next 50 older messages.
- [ ] Message history is stored persistently in the database, not just in memory.
- [ ] Timestamps on historical messages are shown in the user's local timezone.

---

### US-07 — Online Presence Indicators
**Priority:** 🟡 Medium | **Story Points:** 3

> *As a* **room member**, *I want to* **see which users are currently online in a room** *so that* **I know who I'm actively talking to.**

**Acceptance Criteria:**
- [ ] A sidebar or header panel lists all members currently present in the room.
- [ ] Online members show a green indicator; members who left show as offline within 5 seconds.
- [ ] Joining and leaving events broadcast a system message in the chat (e.g., "Ana joined the room").
- [ ] Presence list updates in real time without a page refresh.

---

### US-08 — Leave or Delete a Room
**Priority:** 🟡 Medium | **Story Points:** 2

> *As a* **room member or admin**, *I want to* **leave a room I joined or delete a room I created** *so that* **I can manage my participation and keep the platform tidy.**

**Acceptance Criteria:**
- [ ] Any member can leave a room; they are removed from the presence list immediately.
- [ ] Only the room admin can delete the room; deletion requires a confirmation prompt.
- [ ] When a room is deleted, all members are disconnected and shown a "Room closed" notice.
- [ ] If the admin leaves without deleting, the next longest-standing member becomes admin.

---

### US-09 — Message Reactions
**Priority:** 🟢 Low | **Story Points:** 3

> *As a* **room member**, *I want to* **react to messages with emoji** *so that* **I can respond quickly without cluttering the chat with short replies.**

**Acceptance Criteria:**
- [ ] Hovering/long-pressing a message reveals an emoji reaction picker with at least 6 options.
- [ ] Reactions are displayed as emoji + count beneath the message.
- [ ] Clicking an emoji the user already reacted with toggles it off.
- [ ] Reaction counts update in real time for all room members.

---

### US-10 — User Profile & Avatar
**Priority:** 🟢 Low | **Story Points:** 2

> *As a* **registered user**, *I want to* **set a display name and upload a profile avatar** *so that* **other users can recognize me across different chat rooms.**

**Acceptance Criteria:**
- [ ] Profile page allows editing display name and uploading an image (JPG/PNG, max 2MB).
- [ ] Uploaded avatar is resized and served at 64×64px.
- [ ] Display name and avatar updates are reflected immediately in any active chat room.
- [ ] Users without a custom avatar are shown an auto-generated initial-based placeholder.

---

## Backlog Summary

| ID    | Title                             | Priority | Points |
|-------|-----------------------------------|----------|--------|
| US-01 | User Registration                 | 🔴 High  | 2      |
| US-02 | User Login & Logout               | 🔴 High  | 1      |
| US-03 | Create a Chat Room                | 🔴 High  | 2      |
| US-04 | Browse and Join Public Rooms      | 🔴 High  | 3      |
| US-05 | Send & Receive Real-time Messages | 🔴 High  | 5      |
| US-06 | View Chat History                 | 🔴 High  | 3      |
| US-07 | Online Presence Indicators        | 🟡 Med   | 3      |
| US-08 | Leave or Delete a Room            | 🟡 Med   | 2      |
| US-09 | Message Reactions                 | 🟢 Low   | 3      |
| US-10 | User Profile & Avatar             | 🟢 Low   | 2      |
| **Total** |                               |          | **26** |