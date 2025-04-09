import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template as a string
html_template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Demo App</title>
</head>
<body>
    <h1>Welcome to the Flask Demo App!</h1>
    <p>Type something below and see the magic:</p>
    <form method="POST" action="/">
        <input type="text" name="user_input" placeholder="Enter something" required>
        <button type="submit">Submit</button>
    </form>
    {% if response %}
        <h2>Response: {{ response }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def main():
    response = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        response = f"You entered: {user_input}"
    return render_template_string(html_template, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)