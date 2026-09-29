# student_expert_system.py
# Facts about the student
facts = {
    "CompletedAIProject",
    "GoodAttendance",
    "CompletedCloudCertification",
    "ParticipatesInCodingPractice",
    "StrongProgrammingSkills"
}


# Rules:
# conclusion -> required conditions
rules = {
    "GoodAcademicPerformance": [
        ["GoodAttendance", "StrongProgrammingSkills"]
    ],

    "EligibleForPlacement": [
        ["GoodAcademicPerformance", "CompletedCloudCertification"]
    ],

    "NeedsExtraPractice": [
        ["ParticipatesInCodingPractice", "StrongProgrammingSkills"]
    ],

    "ReadyForTechnicalInterview": [
        ["EligibleForPlacement", "CompletedAIProject"]
    ],

    "RecommendedForAIInternship": [
        ["ReadyForTechnicalInterview", "CompletedAIProject"]
    ]
}


def backward_chaining(goal, visited=None, level=0):
    """
    Prove a goal using backward chaining.
    Returns True if the goal can be proven.
    """

    if visited is None:
        visited = set()

    # Avoid circular reasoning
    if goal in visited:
        return False

    visited.add(goal)

    indent = "  " * level

    # Check whether goal is a known fact
    if goal in facts:
        print(f"{indent}✓ Fact found: {goal}")
        return True

    # Check whether a rule can prove the goal
    if goal not in rules:
        print(f"{indent}✗ No rule found to prove: {goal}")
        return False

    print(f"{indent}Trying to prove: {goal}")

    # Try each rule associated with the goal
    for conditions in rules[goal]:

        print(
            f"{indent}Rule: {goal} <- "
            + " AND ".join(conditions)
        )

        all_conditions_true = True

        for condition in conditions:
            if not backward_chaining(condition, visited.copy(), level + 1):
                all_conditions_true = False
                break

        if all_conditions_true:
            print(f"{indent}✓ Proved: {goal}")
            return True

    print(f"{indent}✗ Could not prove: {goal}")
    return False


# ---------------------------------------
# Select the goal
# ---------------------------------------

goal = "RecommendedForAIInternship"

print("=" * 55)
print("STUDENT ACADEMIC GUIDANCE EXPERT SYSTEM")
print("=" * 55)

print("\nStudent Facts:")
for fact in facts:
    print("-", fact)

print("\nSelected Goal:")
print("-", goal)

print("\nReasoning Steps:")
print("-" * 55)

result = backward_chaining(goal)

print("-" * 55)

# Final conclusion
if result:
    print("\nFinal Conclusion:")
    print(f"The student IS {goal}.")
else:
    print("\nFinal Conclusion:")
    print(f"The student is NOT {goal}.")
