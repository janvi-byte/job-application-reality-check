from utils.evaluation import evaluate_candidate

print("=== Job Application Assistant ===\n")

job_role = input("Enter job role you are applying for: ")
skills = input("Enter required skills (comma separated): ")

print(f"\nEvaluating readiness for role: {job_role}")
evaluate_candidate(skills)
