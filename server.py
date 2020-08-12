import os

from flask import Flask, render_template, json

app = Flask(__name__)


# CORS(app)

# SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
#     json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
#     data = json.load(open(json_url))
#     return render_template('showjson.jade', data=data)
#

@app.route('/')
def index():
# static/data/test_data.json
    filename = os.path.join(app.static_folder, 'data', 'heroKills.json')

    with open(filename) as test_file:
        data = json.load(test_file)

    return render_template('index.html', data=data)


# @app.route("/getjson")
# def json():
#     data = {"this": "is", "just": "a test"}
#     return data


# @app.route('/my-link/')
# def my_link():
#     print('I got clicked!')
#
#     dotaScript.runScriptFn()
#     # return redirect("http://www.example.com", code=302)
#     return 'Click.'


if __name__ == '__main__':
    app.run(debug=True)
