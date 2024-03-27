from sqlalchemy import create_engine, text
import os

db_connection_string =  os.environ['db_connection_string']

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

     # Convert result rows to dictionaries
    jobs = []
    for row in result.fetchall():
          row_dict = {}
          for column, value in zip(result.keys(), row):
              row_dict[column] = value
          jobs.append(row_dict)
    return jobs