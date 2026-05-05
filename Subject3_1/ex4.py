from flask import Flask, render_template, request

app = Flask(__name__)

# 입력 페이지
@app.route('/')
def index():
    return render_template('input.html')

# 결과 페이지
@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    student = request.form['student_number']
    gender = request.form['gender']
    major = request.form['major']
    languages = request.form.getlist('languages')

    return render_template(
        'result.html',
        name=name,
        student_number=student,
        gender=gender,
        major=major,
        languages=languages
    )

if __name__ == '__main__':
    app.run(debug=True)
