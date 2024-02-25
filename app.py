from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    user_input = request.form['user_input']
    python_output = subprocess.run(['python', 'tw-sentimental.py', user_input], capture_output=True).stdout.decode()
    return render_template('index.html', output=python_output)

if __name__ == '__main__':
    app.run(debug=True)
