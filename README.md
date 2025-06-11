In this repository, you can find some UI and API tests for the website 'Teveclub', using Playwright/Pytest/Requests.

Features:
API Sanity Check: Verifies the Teveclub server's status with a simple API check. If the website is up, the UI tests will proceed. This is crucial since the Teveclub server can experience issues intermittently.

Teve Interaction:
- Login: Logs in to the selected Teve.
- Feeding: Gives the Teve food and drink.
- Trick Learning: Teaches the Teve a trick. After the trick is learned, the next trick in line is selected automatically.

Requirements
- Python 3.x
- Playwright library 
- Pytest library
- Requests library 
