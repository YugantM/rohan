from flask import Flask, render_template,request, jsonify
import random,os


app = Flask(__name__)


@app.route("/recieve", methods=['POST','GET'])
def home():

    input_json = request.get_json(force=True) 
        
    print(input_json)
    
    corr = random.randint(-10, 10)
    input_json['correction'] = corr
    input_json['value'] = 230 + corr

    return jsonify(input_json)



if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=False,port=5001)