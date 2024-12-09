from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL


app = Flask(__name__)


def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Minachy1',
        database='quiz_app'
    )
    return connection


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        score = 0

        
        answer1 = request.form.get('q1')
        answer2 = request.form.get('q2')
        answer3 = request.form.get('q3')
        answer4 = request.form.get('q4')

        
        if answer1 == "C":
            score += 1
        if answer2 == "A":
            score += 1
        if answer3 == "B":
            score += 1
        if answer4 == "A":
            score += 1

        
        name = request.form.get('name')
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO quiz_scores (name, score) VALUES (%s, %s)", (name, score))
        connection.commit()
        cursor.close()
        connection.close()

        return redirect(url_for('result', score=score))

    return render_template('quiz.html')


@app.route('/result')
def result():
    score = request.args.get('score', type=int)
    return render_template('result.html', score=score)

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
