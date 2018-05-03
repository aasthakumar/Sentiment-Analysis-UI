from flask import Flask, jsonify, request, Response, render_template
from urllib.parse import urlparse
from model import model

app = Flask(__name__)

@app.route('/')
def student():
   return render_template('webpage.html')

@app.route('/sentiments', methods=['POST','GET'])
def getsentiments():
    if request.method == 'POST':
        review = request.form
        for k, v in review.items():
            val = v
        print(val)
        result = model(val)
        print(result)
        if result == [0]:
            result = "Negative"
            return render_template('result1.html',result = result)
        else:
            result = "Positive"
            return render_template('result.html',result = result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
