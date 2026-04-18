from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# -----------------------------
# SIMPLE QUESTION BANK
# -----------------------------
questions = [
    {
        "question": "Tell me about yourself.",
        "keywords": ["student", "computer science", "skills", "experience"]
    },
    {
        "question": "Why do you want this job?",
        "keywords": ["interest", "career", "growth", "company"]
    },
    {
        "question": "What is your strength?",
        "keywords": ["strength", "problem solving", "teamwork", "communication"]
    }
]

current_index = 0


# -----------------------------
# NLP ANALYSIS FUNCTION (SIMPLE)
# -----------------------------
def analyze_answer(answer, keywords):
    answer = answer.lower()

    score = 0
    matched = []

    for kw in keywords:
        if kw.lower() in answer:
            score += 1
            matched.append(kw)

    if len(keywords) == 0:
        return 0, "No evaluation available"

    final_score = (score / len(keywords)) * 10

    if final_score >= 7:
        feedback = "Good answer 👍"
    elif final_score >= 4:
        feedback = "Average answer ⚠️ (add more key points)"
    else:
        feedback = "Weak answer ❌ (too few relevant points)"

    return round(final_score, 1), feedback


# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def home():
    global current_index
    question = questions[current_index]["question"]
    return render_template("index.html", question=question)


@app.route("/next-question")
def next_question():
    global current_index
    current_index = (current_index + 1) % len(questions)
    return jsonify({
        "question": questions[current_index]["question"]
    })


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json

    answer = data["answer"]
    question_index = data["question_index"]

    keywords = questions[question_index]["keywords"]

    score, feedback = analyze_answer(answer, keywords)

    return jsonify({
        "score": score,
        "feedback": feedback
    })


if __name__ == "__main__":
    app.run(debug=True)