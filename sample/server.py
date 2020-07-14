from flask import Flask, render_template
from sample import dotaScript
from flask_cors import CORS




app = Flask(__name__)

CORS(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  print ('I got clicked!')

  dotaScript.runScriptFn()
  # return redirect("http://www.example.com", code=302)
  return 'Click.'

if __name__ == '__main__':
  app.run(debug=True)
