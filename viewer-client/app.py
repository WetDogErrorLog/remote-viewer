from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    # Check if db exists
    # If not: create db.

    # Display a button for import local configs
    # Allow manual entry (target IP, select adapter as enum from dropdown)
    return "<p>Hello, world! Lets fuck shit up!</p>"

if __name__ == "__main__":
    app.run(debug=True)

