Bug ID: BUG-001
Title: Register button redirects to external YouTube link
Severity: High
Status: Open

Description:
When a user clicks the "Register" button on the main landing/login page, the application fails to route them to the registration form. Instead, the href or onClick event is improperly linked to an external YouTube URL.

Steps to Reproduce:

1. Navigate to the main login/landing page.
2. Locate the "Register" button.
3. Click the button.
4. Observe the browser redirecting away from the local application to a YouTube video.

Expected Behavior:
Clicking the "Register" button should load the registration component or route the user to the /register page so they can create an account.

Actual Behavior:
The user is taken entirely off the application and redirected to youtube.com.