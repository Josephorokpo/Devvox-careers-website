# Import necessary modules
from sqlalchemy import create_engine, text
import os

# Get the database connection string from environment variables
db_connection_string = os.environ['DB_CONNECTION_STRING']

# Create a SQLAlchemy engine that will interact with the database
engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})

# Function to load all jobs from the database
def load_jobs_from_db():
  with engine.connect() as conn:
    # Execute the SQL query
    result = conn.execute(text("select * from jobs"))
    jobs = []
    # Iterate over the result and append each job to the jobs list
    for row in result.all():
      jobs.append(dict(zip(result.keys(), row)))
    return jobs

# Function to load a specific job from the database using its id
def load_job_from_db(id):
  with engine.connect() as conn:
    # Execute the SQL query
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),
                          {'val': id})
    rows = result.all()
    # If no rows are returned, return None
    if len(rows) == 0:
      return None
    else:
      # Otherwise, return the first row
      return dict(zip(result.keys(), rows[0]))

# Function to add an application to the database
def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    # Define the SQL query and the parameters
    query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")
    params = {
      'job_id': job_id,
      'full_name': data['full_name'],
      'email': data['email'],
      'linkedin_url': data['linkedin_url'],
      'education': data['education'],
      'work_experience': data['work_experience'],
      'resume_url': data['resume_url']
    }
    # Execute the SQL query with the parameters
    conn.execute(query, params)
