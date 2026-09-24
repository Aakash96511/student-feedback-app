from flask import Flask, render_template, request

app = Flask(__name__)

feedbacks = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()
        feedback = request.form.get("feedback", "").strip()

        if name and email and course and feedback:
            feedbacks.append({
                "name": name,
                "email": email,
                "course": course,
                "feedback": feedback
            })

    return render_template("index.html", feedbacks=feedbacks)


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)