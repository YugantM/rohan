from flask import Flask, render_template, request
import requests
import random, json, os

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():

    return render_template('index.html')


@app.route('/send', methods=["GET", "POST"])

def sending():
    
    if request.method == 'POST':
        
        data = request.form['value']

        print(data)

        dictToSend = {}
        rand = random.randint(0, 40)
        dictToSend['random'] = rand
        dictToSend['value'] = int(data) + rand

        if 210 <= int(data) <= 260:

            res = requests.post('http://172.17.0.1:5001/recieve', json=dictToSend)

            print(res.text)
        else:

            return "Error"

    return res.text


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=5000)