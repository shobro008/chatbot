from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sqlite3
from fuzzywuzzy import process  # For fuzzy matching

app = Flask(__name__)
CORS(app)  # Allow requests from all origins

# Synonym mapping for flexibility
synonyms = {
    "hr": "Human Resources",
    "human resources": "Human Resources",
    "sales rep": "Sales Representative",
    "team lead": "Manager",
    "developer": "Engineer"
}

# List of valid departments for fuzzy matching
departments = ["Sales", "Engineering", "Marketing", "Human Resources"]

# Database helper function
def query_db(query, args=(), one=False):
    conn = sqlite3.connect('company_large.db')  # Ensure this is the correct path to your database
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(query, args)
    rv = cursor.fetchall()
    conn.close()
    return (rv[0] if rv else None) if one else rv

# Preprocess query for synonyms and standardization
def preprocess_query(query):
    query = query.lower()
    for key, value in synonyms.items():
        query = query.replace(key.lower(), value.lower())
    return query

# Fuzzy matching for department names
def get_closest_match(query, choices):
    match, score = process.extractOne(query, choices)
    if score > 80:  # Set a threshold for matching accuracy
        return match
    return None

# Root route to serve the frontend HTML
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Chatbot route
@app.route('/chatbot', methods=['GET'])
def chatbot():
    query = request.args.get('query', '')
    print(f"Received query: {query}")  # Debugging

    response = {"response": "Sorry, I did not understand the query. Please try again."}

    try:
        if query:
            # Preprocess the query for synonyms and standardization
            query = preprocess_query(query)

            # Extract department name using fuzzy matching
            department = None
            for word in query.split():
                closest_match = get_closest_match(word.capitalize(), departments)
                if closest_match:
                    department = closest_match

            # Query for employees in a specific department
            if department and "all employees" in query:
                sql = "SELECT Name FROM Employees WHERE LOWER(Department) = LOWER(?)"
                result = query_db(sql, (department,))
                if result:
                    response["response"] = [r["Name"] for r in result]
                else:
                    response["response"] = f"No employees found in the {department} department."

            # Query for the manager of a department
            elif department and "manager" in query:
                sql = """
                    SELECT Name FROM Employees 
                    WHERE LOWER(Department) = LOWER(?) AND LOWER(Position) LIKE '%manager%'
                """
                result = query_db(sql, (department,))
                if result:
                    response["response"] = [r["Name"] for r in result]
                else:
                    response["response"] = f"No manager found in the {department} department."

            # Query for employees hired after a certain date
            elif "hired after" in query:
                date = query.split("hired after ")[1]
                sql = "SELECT Name FROM Employees WHERE Hire_Date > ?"
                result = query_db(sql, (date,))
                if result:
                    response["response"] = [r["Name"] for r in result]
                else:
                    response["response"] = f"No employees found hired after {date}."

            # Query for total salary expense of a department
            elif department and "total salary expense" in query:
                sql = "SELECT SUM(Salary) AS TotalSalary FROM Employees WHERE LOWER(Department) = LOWER(?)"
                result = query_db(sql, (department,))
                total_salary = result[0]["TotalSalary"] if result[0]["TotalSalary"] else 0
                response["response"] = f"Total salary expense for {department} department: ${total_salary}"

        else:
            response["response"] = "Please provide a valid query."

    except Exception as e:
        response["response"] = f"An error occurred: {str(e)}"

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
