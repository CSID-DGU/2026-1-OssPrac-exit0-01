from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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