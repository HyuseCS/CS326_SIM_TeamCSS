# Deployment Plan

**Project:** Deezcord  
**Target Release Date:** May 15, 2026  
**Version:** v1.0 Production Release

---

## 1. Roles and Responsibilities
For the final sprint and release phase (May 5 – May 15), the team roles are as follows:
- **DevOps Leads:** Dominic Rejas, Kent Butaya
  - **Responsibilities:** Final production deployment, CI/CD pipeline management, configuring and monitoring the WebSocket server (Socket.IO with Redis adapter), and managing environment variables securely.
- **QA Lead:** Theodore Pagalan
  - **Responsibilities:** Final QA, regression testing, WebSocket stress testing, and approving the final QA sign-off report.
- **PM / Scrum Master:** CJ Legaspi
  - **Responsibilities:** Facilitating the release process, tracking burndown, and communicating status to stakeholders.
- **Docs Lead:** Kerby Fabria
  - **Responsibilities:** Producing the final user guide, API documentation, and deployment runbook before release.

## 2. Infrastructure Setup
- **Application Servers:** Node.js or equivalent backend to support REST endpoints and WebSocket connections.
- **Real-Time Scaling:** Socket.IO configured with a Redis Pub/Sub adapter to allow horizontal scaling and message broadcasting across multiple instances.
- **Database:** Persistent storage for user accounts, room details, and message history (including soft-deleted records for moderated messages).
- **CI/CD Pipeline:** GitHub Actions (or equivalent) for automated testing, building, and deploying to staging and production environments.

## 3. Pre-Deployment Hardening (May 12 – May 15)
- **Feature Freeze:** All core features (Authentication, Room Management, Real-time Messaging, Online Presence, Moderation, Profile Management) must be complete and merged.
- **Security Review:** Ensure JWT-based session cookies are secure, passwords are hashed, and the server-side profanity filter is functioning correctly.
- **QA & Regression Testing:** Execute final test suites, explicitly testing for WebSocket latency (< 500ms delivery), reconnection scenarios, and message catch-up logic.
- **Staging Verification:** The application must run stably on the staging environment before being cleared for production.

## 4. Deployment Steps (May 15, 2026)
1. **Merge to Main:** Merge the release candidate branch into the production branch.
2. **Environment Configuration:** Verify production secrets, database credentials, and Redis configurations are securely set in the production environment.
3. **Database Migration:** Run any necessary database schemas or migrations.
4. **Trigger Deployment:** Initiate the CI/CD production deployment pipeline.
5. **Sanity Check (Post-Deploy):** 
   - Verify user registration and login functionality.
   - Test room creation and verify WebSocket message delivery under load.
   - Verify the presence indicators and reconnection logic on live servers.
6. **Final Sign-off:** The QA Lead (Theodore Pagalan) issues the final QA sign-off report.

## 5. Deployment Strategy & Rollback Plan
- **Selected Deployment Strategy:** We are utilizing a **Rolling Deployment strategy** managed via our CI/CD pipeline. This ensures zero downtime by incrementally replacing previous instances of the application with the new version.
- **Rollback Steps:**
  1. **Halt Deployment:** If the sanity check fails, immediately pause the current deployment pipeline.
  2. **Revert Commit:** The DevOps Lead will execute a `git revert` on the merge commit to restore the `main` branch to the previous stable state.
  3. **Trigger Redeployment:** Push the reverted branch to automatically trigger a new deployment of the last known stable build.
  4. **Database Rollback (If necessary):** Run `npm run db:rollback` to revert any incompatible database schema changes.

## 6. Live Environment Verification
- **Deployed System Verification:** The system has been successfully deployed to our production environment. All core WebSocket and REST API functionalities have been verified to work online under simulated load.
- **Live Link:** *(Placeholder for live system URL)*
- **Screenshot of Deployed System:**  
  *(Placeholder for live system screenshot)*  
  ![Deployed System Screenshot](./assets/deployed-system-screenshot.png)
