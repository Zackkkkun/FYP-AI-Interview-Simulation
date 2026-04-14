from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    "Tell me about yourself",
    "What are your strengths?",
    "Describe a time you worked in a team"
]

@app.route("/")
def home():
    return render_template("index.html", question=questions[0])

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    user_answer = data.get("answer")
    question = data.get("question")

    return jsonify({
        "message": f"Question: {question} | Your answer: {user_answer}"
    })

if __name__ == "__main__":
    app.run(debug=True)