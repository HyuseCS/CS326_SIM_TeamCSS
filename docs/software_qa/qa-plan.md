Technical Debt:
1. No persistent data storage: User accounts are only stored in local memory, meaning all registrations are wiped out the moment the page is refreshed.

2. Plaintext password handling: Passwords are being passed and stored in memory exactly as typed, without any hashing or encryption applied.

3. Weak input validation: The registration form accepts potentially invalid email formats or weak passwords without enforcing strict rules before submission.

4. Lack of rate limiting: There are no protections against a user spamming the login or register buttons, which could lead to performance issues or brute-force attempts later.

5. Vague error handling: When authentication fails, the application lacks specific error messages (e.g., "password incorrect" vs. "user not found"), making debugging difficult.

Test Types:
1. Unit Testing: Testing individual, isolated pieces of code to ensure they work correctly on their own. For example, testing a single function that checks if a password is at least 8 characters long.

2. Integration Testing: Testing how different parts of the application interact with each other. For example, testing if clicking the "Submit" button on the register form successfully passes the data to the authentication state manager.