import requests
from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('base.html')

@app.route('/jokes')
def jokes():
  r = requests.get('https://api.chucknorris.io/jokes/random')
  resp = r.json()
  joke = resp['value']
  return render_template('jokes.html', joke=joke)

if __name__ == '__main__':
  app.run(debug=True)