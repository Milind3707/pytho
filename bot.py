from flask import Flask ,request
from flask_ngrok import  run_with_ngrok
app  = Flask(__name__)
run_with_ngrok(app)
@app.route("/")
def hello_word():
    print(__name__)
    cap = request.form.get('get')
    print(cap)

    return    {"name": "milind"}
if __name__ == '__main__':
        app.run()