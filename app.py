from flask import Flask, render_template, request
import openai
import re

app = Flask(__name__)
openai.api_key = "YOUR_OPENAI_API_KEY"

def preprocess_question(question):
    question = question.lower()
    question = re.sub(r'[^\w\s]', '', question)
    return question

def get_answer(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Answer the following question:\n{question}",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    processed = ""
    if request.method == "POST":
        question = request.form.get("question")
        processed = preprocess_question(question)
        answer = get_answer(processed)
    return render_template("index.html", processed=processed, answer=answer)

if __name__ == "__main__":
    app.run(debug=True)
