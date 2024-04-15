# Import necessary modules from Flask and database operations from a custom module
from flask import Flask, render_template, jsonify, request
from database import load_jobs_from_db, load_job_from_db, add_application_to_db

# Create a Flask application instance
app = Flask(__name__)

# Define the route for the homepage
@app.route("/")
def hello_devvox():
  # Load jobs from the database
  jobs = load_jobs_from_db()
  # Render the home page template with the jobs data
  return render_template('home.html', jobs=jobs)

# Define the route for the jobs API endpoint
@app.route("/api/jobs")
def list_jobs():
  # Load jobs from the database
  jobs = load_jobs_from_db()
  # Return the jobs data as JSON
  return jsonify(jobs)

# Define the route for an individual job page
@app.route("/job/<id>")
def show_job(id):
  # Load the job from the database using its id
  job = load_job_from_db(id)

  # If the job doesn't exist, return a 404 error
  if not job:
    return "Not Found", 404

  # Render the job page template with the job data
  return render_template('jobpage.html', job=job)

# Define the route for an individual job's API endpoint
@app.route("/api/job/<id>")
def show_job_json(id):
  # Load the job from the database using its id
  job = load_job_from_db(id)
  # Return the job data as JSON
  return jsonify(job)

# Define the route for applying to a job
@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  # Get the form data from the request
  data = request.form
  # Load the job from the database using its id
  job = load_job_from_db(id)
  # Add the application to the database
  add_application_to_db(id, data)
  # Render the application submitted page with the application and job data
  return render_template('application_submitted.html', 
                         application=data,

                         job=job)
  
# Render the about page template
@app.route('/about')
def about():
    return render_template('about.html')

# Render the contact page template
@app.route('/contact')
def contact():
    return render_template('contact_us.html')

# Run the application
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
