from flask import Flask, render_template, request, redirect, session
from questions import questions

app = Flask(__name__)
app.secret_key = "quizsecret"

@app.route('/')
def home():
    session['score'] = 0
    session['qno'] = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():

    qno = session.get('qno', 0)

    if request.method == 'POST':
        selected = request.form.get('option')

        if selected == questions[qno]['answer']:
            session['score'] += 1

        session['qno'] += 1
        qno = session['qno']

    if qno >= len(questions):
        return redirect('/result')

    return render_template('quiz.html',
                           question=questions[qno],
                           number=qno+1)

@app.route('/result')
def result():
    score = session.get('score', 0)
    total = len(questions)
    return render_template('result.html',
                           score=score,
                           total=total)

if __name__ == '__main__':
    app.run(debug=True)