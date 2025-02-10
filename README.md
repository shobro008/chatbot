text
## Chatbot Project Submission

---

### Project Title: Company Chatbot for Employee and Department Queries

---

### Overview

This project is a **Company Chatbot** designed to answer queries related to employees, departments, and organizational data. The chatbot is built using **Flask** as the backend framework and features a user-friendly frontend interface developed with **HTML, CSS, and JavaScript**. The chatbot interacts with a SQLite database to fetch relevant information and provides responses based on user input.

The primary goal of this project is to create an intelligent chatbot capable of handling various queries about employees, departments, managers, salaries, and more. The chatbot works perfectly when run locally but faced deployment challenges when attempting to host it on Google Cloud App Engine.

---

### Key Features

1.  **Employee Queries**:
    *   Retrieve employee details by department.
    *   Find employees hired after a specific date.
    *   Fetch employees based on their position (e.g., "Who are the Software Engineers?").

2.  **Department Queries**:
    *   Identify the manager of a specific department.
    *   List all employees in a department.
    *   Calculate the total salary expense for a department.

3.  **Database Integration**:
    *   The chatbot uses a SQLite database (`company_large.db`) to store and query employee and department data.

4.  **Frontend Interface**:
    *   A simple web-based interface where users can input their queries.
    *   Queries are processed via AJAX calls to the Flask backend, and responses are displayed dynamically in the chatbox.

5.  **Backend Functionality**:
    *   The backend is powered by Flask and processes user queries through predefined SQL commands.
    *   Includes features like case-insensitive matching, synonym handling, and fuzzy matching for flexibility.

6.  **Local Functionality**:
    *   The chatbot works flawlessly when run locally using `app.py` on port 5000.
    *   Users can access the chatbot via `http://127.0.0.1:5000/` and interact with it seamlessly.

---

### Technologies Used

*   **Backend**: Flask (Python)
*   **Frontend**: HTML, CSS, JavaScript
*   **Database**: SQLite
*   **Other Libraries**:
    *   `Flask-CORS`: To handle cross-origin requests.
    *   `fuzzywuzzy`: For fuzzy matching of user inputs.
    *   `gunicorn`: For running the app in production environments (used during deployment attempts).

---

### Project Structure

project/
│
├── app.py # Flask backend code
├── company_large.db # SQLite database file
├── templates/ # Folder for HTML files
│ └── index.html # Frontend interface
├── requirements.txt # Python dependencies
├── app.yaml # Configuration file for Google App Engine
text

---

### Challenges Faced

1.  **Deployment Issues**:
    *   While the chatbot works perfectly on the local system, deploying it to Google Cloud App Engine resulted in errors.
    *   The primary issue was related to permissions for the App Engine Default Service Account (`chatbot-shobro@appspot.gserviceaccount.com`), which lacked access to necessary resources like storage buckets and databases.

2.  **Database Accessibility**:
    *   Google Cloud App Engine's standard environment has a read-only filesystem except for `/tmp`. This required copying the SQLite database (`company_large.db`) to `/tmp` during runtime.
    *   Despite implementing this solution, deployment still failed due to permission-related issues.

3.  **IAM Configuration**:
    *   The App Engine Default Service Account required roles such as `App Engine Admin`, `Cloud Build Service Account`, `Storage Object Viewer`, and `Storage Object Creator`.
    *   These roles were granted during troubleshooting but did not resolve the deployment issue completely.

4.  **Error Logs During Deployment**:
    *   The error logs indicated that the service account did not have access to the staging bucket (`staging.chatbot-shobro.appspot.com`), which prevented successful deployment.

---

### Current Status

*   The chatbot is fully functional when run locally on a development machine using the command:

python app.py
text

*   It can be accessed at `http://127.0.0.1:5000/` and handles queries as expected.
*   Deployment to Google Cloud App Engine was attempted multiple times but was unsuccessful due to permission-related issues and environment constraints.

---

### How It Works Locally

1.  Start the Flask application by running:

python app.py
text

2.  Open a browser and navigate to:

http://127.0.0.1:5000/
text

3.  Enter queries like:
    *   `"Who is the manager of Sales?"`
    *   `"List all employees in Marketing."`
    *   `"What is the total salary expense for HR?"`

4.  The chatbot processes these queries using SQL commands on the SQLite database (`company_large.db`) and returns appropriate responses in real-time.

---

### Future Improvements

1.  **Deployment Fixes**:
    *   Resolve permission issues for the App Engine Default Service Account on Google Cloud.
    *   Explore alternative hosting platforms like Render or Railway for easier deployment of Flask applications with SQLite databases.

2.  **Database Migration**:
    *   Replace SQLite with a cloud-based database like Google Cloud SQL or Firebase Firestore for better compatibility with cloud environments.

3.  **Enhanced Query Processing**:
    *   Add support for natural language processing (NLP) to make query handling more flexible.
    *   Implement advanced error handling to provide more descriptive error messages.

4.  **Frontend Improvements**:
    *   Enhance the UI/UX of the chatbot interface for better usability.
    *   Add support for voice input/output for accessibility.

---

### Conclusion

This project demonstrates a functional chatbot capable of handling employee and department-related queries effectively when run locally. While deployment challenges prevented hosting it publicly on Google Cloud App Engine, the chatbot's local performance showcases its potential as an intelligent query-handling application.

The project highlights key skills in backend development (Flask), frontend integration (HTML/CSS/JavaScript), database management (SQLite), and cloud deployment troubleshooting (Google Cloud).
