# Team Roles

> **Project:** Real-time Chat Rooms  
> **Team Size:** 5 Members  
> **Role Rotation:** Roles rotate each sprint so every member gains experience across all functions.

---

## Team Members

| Member           | Program / Background            | Contact                          |
|------------------|---------------------------------|----------------------------------|
| Kent Butaya        | BS Computer Science, Year 3     | butaya.kentvincent07@gmail.com         |
| Christian John Legaspi        | BS Computer Science, Year 3     | christianjohn.legaspi@1.ustp.edu.ph         |
| Theodore Pagalan       | BS Computer Science, Yr 3 | pagalan.theodoreustp@gmail.com |
| Carl Dominic Rejas  | BS Computer Science, Year 3     |  rejas.dominic@gmail.com  |
| Kerby Fabria  |   BS Computer Science, Year 3     | kerbyfabriabual@gmail.com |

---

## Role Descriptions

### 🗂 PM / Scrum Master
Facilitates all Scrum ceremonies (planning, stand-ups, review, retro). Manages the backlog, tracks velocity, removes blockers, and communicates sprint status to stakeholders. Acts as the team's process guardian — not a boss, but a servant-leader.

**Key Responsibilities:**
- Run daily stand-ups (strict 15-minute timebox)
- Maintain and groom the product backlog in priority order
- Keep the sprint board and burndown chart up to date
- Escalate blockers unresolved within 24 hours

---

### 🧪 QA Lead
Owns the quality of every feature shipped in the sprint. Writes and executes test cases, manages bug tracking, and enforces the Definition of Done. Given the real-time nature of the project, the QA Lead is also responsible for latency and reconnection scenario testing.

**Key Responsibilities:**
- Write test cases for all sprint stories before development begins
- Execute regression and WebSocket stress tests before sprint review
- Log and prioritize bugs in the issue tracker
- Approve stories as "QA Passed" before the sprint demo

---

### ⚙️ DevOps Lead
Manages the development infrastructure, CI/CD pipeline, and deployment environments. For this project, the DevOps Lead is additionally responsible for configuring and monitoring the WebSocket server (e.g., Socket.IO with Redis adapter for scalability).

**Key Responsibilities:**
- Maintain CI/CD pipeline (GitHub Actions or equivalent)
- Configure and monitor the WebSocket server and Redis pub/sub adapter
- Manage environment variables and secrets securely
- Deploy builds to staging; execute the final production deployment on May 15

---

### 📝 Docs Lead
Ensures all project documentation is accurate, up-to-date, and accessible. Owns the README, API documentation (including WebSocket event schemas), user guide, and meeting notes.

**Key Responsibilities:**
- Document all REST endpoints and WebSocket events after each sprint
- Write and distribute sprint meeting notes within 24 hours
- Maintain the `/docs` folder as the single source of truth
- Produce the final user guide and deployment runbook before release

---

## Role Rotation Schedule

> Given the compressed 4-week timeline, roles rotate once — at the Sprint 1 → Sprint 2 boundary.

| Sprint            | Dates                     | PM / Scrum Master | QA Lead        | DevOps Lead      | Docs Lead        |
|-------------------|---------------------------|-------------------|----------------|------------------|------------------|
| Sprint 1          | Apr 21 – May 2, 2026      | Kent Butaya         | Kerby Fabria | Theodore Pagalan, CJ Legaspi       | Dominic Rejas        |
| Sprint 2 + Release| May 5 – May 15, 2026      | CJ Legaspi         | Theodore Pagalan     | Dominic Rejas, Kent Butaya  | Kerby Fabria        |

> **Note:** Every member holds exactly one unique role per sprint. No member repeats a role across the two cycles.

---

