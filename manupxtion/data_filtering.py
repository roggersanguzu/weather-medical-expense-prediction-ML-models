jobs_data = [
    {'job_title': 'Data Scientist',  'job_skills': ['Python', 'Machine Learning'], 'remote': True},
    {'job_title': 'Data Analyst',  'job_skills': ['Excel', 'SQL'], 'remote': False},
    {'job_title': 'Machine Learning Engineer', 'job_skills': ['Python', 'TensorFlow', 'Keras'], 'remote': True},
    {'job_title': 'Software Developer', 'job_skills': ['Java', 'C++'], 'remote': True},
    {'job_title': 'Data Scientist', 'job_skills': ['R', 'Statistics'], 'remote': False}
]

print(list(filter(lambda job:job['remote'],jobs_data)))