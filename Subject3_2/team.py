from flask import Flask, render_template, request

app = Flask(__name__)

members = [
    {
        "id": 1,
        "name": "김보성",
        "major": "정보통신공학과",     
        "role": "Subject3_1 담당",
        "email": "boseong@example.com",
        "github": "https://github.com/BoseongKim02",
        "skills": [
            {"icon": "devicon-python-plain colored", "name": "Python"},
            {"icon": "devicon-flask-original", "name": "Flask"}
        ]
    },
    {
        "id": 2,
        "name": "한규민",
        "major": "정보통신공학과",
        "role": "Subject3_2의 HTML 디자인 담당",
        "email": "gyumin@example.com",
        "github": "https://github.com/hgm0827",
        "skills": [
            {"icon": "devicon-python-plain colored", "name": "Python"},
            {"icon": "devicon-github-original", "name": "GitHub"}
        ]
    },
    {
        "id": 3,
        "name": "김현진",
        "major": "정보통신공학과",
        "role": "Subject3_2의 Flask 코드 담당",
        "github": "https://github.com/guswls-714",
        "email": "hyunjin@example.com",
        "skills": [
            {"icon": "devicon-html5-plain colored", "name": "HTML"},
            {"icon": "devicon-bootstrap-plain colored", "name": "Bootstrap"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', members=members)

@app.route('/input', methods=['GET'])
def input_page():
    return render_template('input.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form.get('Name')
    student_number = request.form.get('StudentNumber')
    gender = request.form.get('Gender')
    major = request.form.get('major')
    languages = request.form.getlist('languages')
    return render_template('result.html',
        name=name,
        student_number=student_number,
        gender=gender,
        major=major,
        languages=languages)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)