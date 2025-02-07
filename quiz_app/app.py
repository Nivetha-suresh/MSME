from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

questions = [
    "1. What is the capital of India?",
    "2. How many states in India?",
    "3. Who is the first Governor of Tamil Nadu?",
    "4. Who is the current president of India?"
]

choices = [
    ('A: Delhi', 'B: Kerala', 'C: Tamil Nadu', 'D: Punjab'),
    ('A: 28', 'B: 27', 'C: 25', 'D: 29'),
    ('A: Ujjal Singh', 'B: K.K. Shah', 'C: Mohan Lal', 'D: Annadurai'),
    ('A: Droupadi Murmu', 'B: Ramnath Govind', 'C: Jaswanth Singh', 'D: Abdul Kalam')
]

answers = ["A", "A", "D", "A"]  # Correct answers

@app.route('/')
def index():
    return render_template('quiz.html', questions=questions, choices=choices)

@app.route('/submit', methods=['POST'])
def submit():
    user_answers = request.form.getlist('answers')
    score = 0
    for i, user_answer in enumerate(user_answers):
        if user_answer == answers[i]:
            score += 1
    return f'Your score is: {score}/{len(answers)}'

if __name__ == '__main__':
    app.run(debug=True)