from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def calculator():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['txt']
    result = eval(expression)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
