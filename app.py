from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)  # Allow requests from all origins

# Database helper function
def query_db(query, args=(), one=False):
    conn = sqlite3.connect('company_large.db')  # Ensure this is the correct path to your database
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Route for chatbot interaction
@app.route('/chatbot', methods=['GET'])
def chatbot():
    query = request.args.get('query', '')
    print(f"Received query: {query}")  # Debugging

    response = {"response": "Sorry, I did not understand the query. Please try again."}

    try:
        if query:
            # Query for employees in a specific department
            if "all employees in the" in query and "department" in query:
                department = query.split('in the ')[1].split(' department')[0]
                print(f"Searching employees in department: {department}")  # Debugging
                sql = "SELECT Name FROM Employees WHERE Department = ?"
                result = query_db(sql, (department,))
                if result:
                    response = {"response": [r['Name'] for r in result]}
                else:
                    response = {"response": f"No employees found in the {department} department."}

            # Query for the manager of a department
            elif "manager of the" in query and "department" in query:
                department = query.split('manager of the ')[1].split(' department')[0]
                print(f"Searching manager in department: {department}")  # Debugging
                sql = "SELECT Name FROM Employees WHERE Department = ? AND Position LIKE '%Manager%'"
                result = query_db(sql, (department,))
                if result:
                    response = {"response": [r['Name'] for r in result]}
                else:
                    response = {"response": f"No manager found in the {department} department."}

            # Query for employees hired after a certain date
            elif "hired after" in query:
                date = query.split('hired after ')[1]
                print(f"Searching for employees hired after: {date}")  # Debugging
                sql = "SELECT Name FROM Employees WHERE HireDate > ?"
                result = query_db(sql, (date,))
                if result:
                    response = {"response": [r['Name'] for r in result]}
                else:
                    response = {"response": "No employees found hired after the specified date."}

            # Query for the total salary expense for a department
            elif "total salary expense for the" in query and "department" in query:
                department = query.split('for the ')[1].split(' department')[0]
                print(f"Calculating salary expense for department: {department}")  # Debugging
                sql = "SELECT SUM(Salary) FROM Employees WHERE Department = ?"
                result = query_db(sql, (department,))
                if result[0][0] is not None:
                    response = {"response": f"Total salary expense for {department} department: ${result[0][0]}"}
                else:
                    response = {"response": f"No salary data found for {department} department."}

        else:
            response = {"response": "Please provide a valid query."}

    except Exception as e:
        response = {"response": f"An error occurred: {str(e)}"}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
