from flask import Flask, render_template

app = Flask(__name__, template_folder='webpages')

'''
to start flask server (from terminal)
set FLASK_APP=maybe.py
set FLASK_DEBUG=1
flask run
'''

@app.route('/')
def home():
    return render_template('LandingPage.html')