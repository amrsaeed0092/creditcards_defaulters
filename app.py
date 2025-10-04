from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug=True, port=5000)
