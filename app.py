import requests
from flask import Flask, url_for, render_template, request, jsonify
app = Flask(__name__)
students = {}

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

@app.route('/api', methods=['GET'])
def get_students():
  return jsonify(students)

@app.route('/api', methods=['POST'])
def add_student():
  added = {}
  student = {k:v for k,v in request.args.items()}
  if student not in students.values():
    idx = len(students)
    added[idx if idx not in students else idx + 1] = student
    students[idx if idx not in students else idx + 1] = student
  return jsonify({"added": added, "current": students})

@app.route('/api', methods=['DELETE'])
def delete_student():
  deleted = {}
  student = {k:v for k,v in request.args.items()}
  try:
    for k,v in students.items():
      if v == student:
        students.pop(k)
        deleted[len(deleted)] = student
  except:
      pass
  return jsonify({"deleted": deleted, "current": students})

if __name__ == '__main__':
  app.run(debug=True)