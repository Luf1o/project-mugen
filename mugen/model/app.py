import csv
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
from agent import invoke_agent

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

# Function to validate username and password from CSV
# Function to validate username and password from CSV
def validate_user(username, password):
    print("Validating user",username,password) 
    try:
        with open('users.csv', mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            for row in csv_reader:
                print(row[0],row[1] )
                if len(row) >= 2 and row[0] == username and row[1] == password:
                    return True
        return False
    except FileNotFoundError:
        print("User database not found.")
        return False
    except Exception as e:
        print(f"Error validating user: {e}")
        return False



# Function to add a new user to the CSV
def add_user(username, password):
    try:
        with open('users.csv', mode='a', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password])
    except FileNotFoundError:
        with open('users.csv', mode='w+', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['username', 'password'])
            csv_writer.writerow([username, password])

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        print("user validation",validate_user(username,password))
        if validate_user(username, password):
            return "Login Succesfull",200 
            #return redirect(url_for('home'))  # Redirect to /chat if valid
        else:
            return  "Invalid Username or Password", 401
            """error_message = "Incorrect username or password!"  # Updated error message
            return render_template("login.html", error_message=error_message)"""
    
    return render_template("login.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Add the new user to the CSV file
        add_user(username, password)
        return redirect(url_for('login'))  # Redirect to login page after successful registration
    
    return render_template("register.html")

@app.route("/chat")
def home():
    return render_template("chat.html")

@socketio.on("user_message")
def handle_user_message(data):
    try:
        user_input = data.get("message", "")
        if not user_input:
            emit("bot_response", {"response": "Empty input"}, broadcast=True)
            return

        # Get the response from the agent
        agent_response = invoke_agent(user_input)
        emit("bot_response", {"response": agent_response}, broadcast=True)
    except Exception as e:
        emit("bot_response", {"response": f"Error: {str(e)}"}, broadcast=True)

if __name__ == "__main__":
    socketio.run(app, debug=True)
