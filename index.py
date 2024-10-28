from flask import Flask, request, app,render_template
from flask import Response


application = Flask(__name__)
app=application

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False)
