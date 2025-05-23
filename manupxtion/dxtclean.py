from datetime import datetime
import ast

data_science_jobs = [
    {'job_title': 'Data Scientist', 'job_skills': "['Python', 'SQL', 'Machine Learning']", 'job_date': '2023-05-12'},
    {'job_title': 'Machine Learning Engineer', 'job_skills': "['Python', 'TensorFlow', 'Deep Learning']", 'job_date': '2023-05-15'},
    {'job_title': 'Data Analyst', 'job_skills': "['SQL', 'R', 'Tableau']", 'job_date': '2023-05-10'},
    {'job_title': 'Business Intelligence Developer', 'job_skills': "['SQL', 'PowerBI', 'Data Warehousing']", 'job_date': '2023-05-08'},
    {'job_title': 'Data Engineer', 'job_skills': "['Python', 'Spark', 'Hadoop']", 'job_date': '2023-05-18'},
    {'job_title': 'AI Specialist', 'job_skills': "['Python', 'PyTorch', 'AI Ethics']", 'job_date': '2023-05-20'}
]

print(datetime.now())
# Convert the job_date string to a datetime object because it takes in the datetim string and then the format that is needed.
print(data_science_jobs[0]['job_date'])
clean_date=(data_science_jobs[0]['job_date'])
print(datetime.strptime(clean_date,'%Y-%m-%d'))

for job in data_science_jobs:
   job['job_date']=datetime.strptime(job['job_date'],'%Y-%m-%d')
   print(data_science_jobs)


# Here i Used the ast for converting strings to lists.
for job in data_science_jobs:
   job['job_skills']=ast.literal_eval(job['job_skills'])
   print(data_science_jobs) 