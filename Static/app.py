from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to a secure random key
app.permanent_session_lifetime = timedelta(minutes=30)

# ---------- INDEX PAGE ----------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- LOGIN ----------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Dummy login credentials (replace with database check)
        if username == "admin" and password == "admin123":
            session.permanent = True
            session["user"] = username
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("index"))

# ---------- HOME PAGE ----------
@app.route("/home")
def home():
    if "user" in session:
        return render_template("home.html", user=session["user"])
    else:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

# ---------- DASHBOARD ----------
@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    else:
        flash("Please log in first", "warning")
        return redirect(url_for("login"))

# ---------- SENTIMENT TEST ----------
@app.route("/sentimenttest", methods=["GET", "POST"])
def sentimenttest():
    sentiment_result = None
    if request.method == "POST":
        text = request.form["text"]
        # Dummy sentiment logic (replace with AI model)
        if "good" in text.lower():
            sentiment_result = "Positive"
        elif "bad" in text.lower():
            sentiment_result = "Negative"
        else:
            sentiment_result = "Neutral"

    return render_template("sentimenttest.html", result=sentiment_result)

# ---------- CHATBOT ----------
@app.route("/chat", methods=["GET", "POST"])
def chat():
    bot_response = None
    if request.method == "POST":
        user_message = request.form["message"]
        # Dummy chatbot logic (replace with IBM Granite API)
        bot_response = f"You said: {user_message} (AI reply here)"
    return render_template("chat.html", response=bot_response)

# ---------- RUN APP ----------
if __name__ == "__main__":
    app.run(debug=True)
