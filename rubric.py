def generate_rubric_from_question(topic,question,job_title):
    junior_prompt = f"You are a junior {job_title}. Answer the following question: {question}\n\n"
    mid_level_prompt = f"You are a mid-level {job_title}. Answer the following question: {question}\n\n"
    senior_prompt = f"You are a senior {job_title}. Answer the following question: {question}\n\n"

    interviewer_rubric = f"""You are an interviewer. You have asked the following question to a candidate: 

{question}

What is a rubric for what you would look for in a candidate's answer to determine whether they had no knowledge, some knowledge, competent knowledge, or advanced knowledge of {topic}? 
"""

def generate_project_rubric_from_description(course_topic,project):
    junior_prompt = f"You are a sophmore in college. You have been given the following project: {project}\n\nDescribe a summary of what you've turned in for this project.\n\n"
    mid_level_prompt = f"You are a junior in college. You have been given the following project: {project}\n\nDescribe a summary of what you've turned in for this project.\n\n"
    senior_prompt = f"You are a senior in college. You have been given the following project: {project}\n\nDescribe a summary of what you've turned in for this project.\n\n"
    industry_prompt = f"You are an industry professional. You have been given the following project: {project}\n\nDescribe a summary of what you've turned in for this project.\n\n"

    interviewer_rubric = f"""You are teacher. You have asked the following question to a your students: 

{project}

What is a rubric that you would use to grade a student's project, to determine if they had no mastery, some mastery, competent mastery, or advanced mastery of {topic}? 
"""