from flask import Flask, render_template
from flask import request, jsonify
from extractive_summarization import Extractive_Summarization
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        text = request.form['itext']
        output = Extractive_Summarization.run_summarization(text)
        #output = text[::-1]
        return render_template('index.html', output=output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=False)
