from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    input_message = request.form.get('message')
    reply = input_message
    return reply

if __name__ == '__main__':
    app.run()