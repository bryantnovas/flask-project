import requests
from flask import Flask, url_for, render_template, request
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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    return render_template('form.html', name=name, email=email,message=message)
  else:
    return render_template('form.html')

if __name__ == '__main__':
  app.run(debug=True)