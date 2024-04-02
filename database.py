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
    jobs = []
    for row in result.fetchall():
          row_dict = {}
          for column, value in zip(result.keys(), row):
              row_dict[column] = value
          jobs.append(row_dict)
    return jobs
    
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val"), {"val": id}
        )
        rows = result.fetchall()
        print("Rows fetched for ID:", id, ":", rows)
        if len(rows) == 0:
            return None
        else:
            job_dicts = []
            for row in rows:
                job_dict = {}
                for column, value in zip(result.keys(), row):
                    job_dict[column] = value
                job_dicts.append(job_dict)
            return job_dicts