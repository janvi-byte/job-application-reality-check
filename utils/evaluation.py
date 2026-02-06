def evaluate_candidate(skills_input):
    skills = skills_input.lower().split(",")
    skills = [skill.strip() for skill in skills]

    total_score = 0
    max_score = len(skills) * 3

    print("\nRate your confidence for each skill:")
    print("0 = Just started")
    print("1 = Basic understanding")
    print("2 = Comfortable")
    print("3 = Strong\n")

    for skill in skills:
        score = int(input(f"{skill}: "))
        total_score += score

    readiness = (total_score / max_score) * 100

    print("\n--- Evaluation Result ---")
    print("Readiness Percentage:", round(readiness, 2), "%")

    if readiness >= 70:
        print("\nAdvice: You are ready to apply ")
        print("- Revise core concepts")
        print("- Practice interview questions")

    elif readiness >= 40:
        print("\nAdvice: You can apply, but prepare well")
        print("- Revise fundamentals")
        print("- Be honest about your learning stage")
        print("- Prepare small project explanations")

    else:
        print("\nAdvice: Not recommended to apply yet")
        print("- Focus on learning basics")
        print("- Build practice projects")
