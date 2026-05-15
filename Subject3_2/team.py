from flask import Flask, render_template, request, abort

app = Flask(__name__)

members = [
    {
        "id": 1,
        "name": "김보성",
        "major": "정보통신공학과",     
        "role": "Coordinator 담당",
        "phone": "010-0000-0000",
        "email": "boseong@example.com",
        "github": "https://github.com/BoseongKim02",
        "photo": "https://via.placeholder.com/150",
        "intro": "팀의 조율을 담당하고 있는 김보성입니다.",
        "mbti": "ENTJ",
        "introduce": "안녕하세요! 팀의 조율을 담당하고 있는 김보성입니다.",
        "skills": [
            {"icon": "devicon-python-plain colored", "name": "Python"},
            {"icon": "devicon-flask-original", "name": "Flask"}
        ]
    },
    {
        "id": 2,
        "name": "한규민",
        "major": "정보통신공학과",
        "role": "Recorder 담당",
        "phone": "010-0000-0000",
        "email": "gyumin@example.com",
        "github": "https://github.com/hgm0827",
        "photo": "https://via.placeholder.com/150",
        "intro": "기록을 담당하고 있는 한규민입니다.",
        "mbti": "ISTJ",
        "introduce": "안녕하세요! 기록을 담당하고 있는 한규민입니다.",
        "skills": [
            {"icon": "devicon-python-plain colored", "name": "Python"},
            {"icon": "devicon-github-original", "name": "GitHub"}
        ]
    },
    {
        "id": 3,
        "name": "김현진",
        "major": "정보통신공학과",
        "role": "Gatekeeper, Timer 담당",
        "phone": "010-0000-0000",
        "email": "hyunjin@example.com",
        "github": "https://github.com/guswls-714",
        "photo": "https://via.placeholder.com/150",
        "intro": "Gatekeeper와 Timer를 담당하고 있는 김현진입니다.",
        "mbti": "INFP",
        "introduce": "안녕하세요! Gatekeeper와 Timer를 담당하고 있는 김현진입니다.",
        "skills": [
            {"icon": "devicon-html5-plain colored", "name": "HTML"},
            {"icon": "devicon-bootstrap-plain colored", "name": "Bootstrap"}
        ]
    }
]

@app.route('/')
def index():
    return render_template('index.html', members=members)

@app.route('/team')
def team():
    return render_template('team.html', members=members)

@app.route('/member/<int:member_id>')
def member_detail(member_id):
    member = next((m for m in members if m["id"] == member_id), None)
    if member is None:
        abort(404)
    return render_template('member.html', member=member)

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
    app.run(host='0.0.0.0', port=5000, debug=True)