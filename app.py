from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Abuja, Nigeria',
    'salary': 'N50000'
  },
  {
    'id': 2,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 'N120000'
  },
  {
    'id': 3,
    'title': 'Data Scientist',
    'location': 'Lagos, Nigeria',
    'salary': 'N100000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'New York, USA',
    'salary': '$150000'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name="Devvox")

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)