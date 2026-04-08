from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_answer = data.get("answer")

    return jsonify({
        "message": f"You said: {user_answer}"
    })

if __name__ == "__main__":
    app.run(debug=True)