from typing import Tuple, Dict

EDUCATION_POINTS = {
    "high school": 0,
    "associate": 5,
    "bachelor": 10,
    "master": 15,
    "phd": 20,
}

WEIGHTS = {
    "education": 0.20,
    "experience": 0.20,
    "skills": 0.30,
    "certifications": 0.05,
    "interview": 0.25,
}

DECISION_THRESHOLD = 70.0  # overall percentage required to consider candidate for hire


def get_positive_int(prompt: str, min_v: int = 0, max_v: int | None = None) -> int:
    while True:
        try:
            v = int(input(prompt).strip())
            if v >= min_v and (max_v is None or v <= max_v):
                return v
        except ValueError:
            pass
        rng = f" (between {min_v} and {max_v})" if max_v is not None else f" (>= {min_v})"
        print(f"Please enter a valid integer{rng}.")


def get_positive_float(prompt: str, min_v: float = 0.0, max_v: float | None = None) -> float:
    while True:
        try:
            v = float(input(prompt).strip())
            if v >= min_v and (max_v is None or v <= max_v):
                return v
        except ValueError:
            pass
        rng = f" (between {min_v} and {max_v})" if max_v is not None else f" (>= {min_v})"
        print(f"Please enter a valid number{rng}.")


def get_education_level() -> str:
    options = ", ".join(k.title() for k in EDUCATION_POINTS.keys())
    while True:
        s = input(f"Education level ({options}): ").strip().lower()
        if s in EDUCATION_POINTS:
            return s
        print("Please choose a valid education level from the list.")


def get_applicant_input() -> Dict:
    name = input("Applicant name (optional): ").strip()
    # Collect only objective features used in scoring
    education = get_education_level()
    years_exp = get_positive_float("Years of relevant experience: ", 0.0, 50.0)
    skills_match = get_positive_float("Skills match percentage (0-100): ", 0.0, 100.0)
    certifications = get_positive_int("Number of relevant certifications: ", 0, 20)
    interview_score = get_positive_float("Interview score (0-10): ", 0.0, 10.0)

    return {
        "name": name,
        "education": education,
        "years_exp": years_exp,
        "skills_match": skills_match,
        "certifications": certifications,
        "interview_score": interview_score,
    }


def compute_score(app: Dict) -> Tuple[float, Dict[str, float]]:
    # normalize component scores to 0-100
    edu_pts = EDUCATION_POINTS[app["education"]]
    edu_score = (edu_pts / max(EDUCATION_POINTS.values())) * 100

    exp_score = min(app["years_exp"], 20.0) / 20.0 * 100  # cap at 20 years

    skills_score = app["skills_match"]  # already 0-100

    cert_score = min(app["certifications"], 5) / 5.0 * 100  # cap at 5 relevant certs

    interview_score = app["interview_score"] / 10.0 * 100

    components = {
        "education": edu_score,
        "experience": exp_score,
        "skills": skills_score,
        "certifications": cert_score,
        "interview": interview_score,
    }

    overall = sum(components[k] * WEIGHTS[k] for k in WEIGHTS)
    return overall, components


def print_result(app: Dict, overall: float, components: Dict[str, float]) -> None:
    print("\n--- Applicant Evaluation ---")
    name = app["name"] or "<unnamed>"
    print(f"Applicant: {name}")
    for k, v in components.items():
        print(f"  {k.title():13}: {v:.1f}% (weight {WEIGHTS[k]:.2f})")
    print(f"Overall score: {overall:.1f}%")
    decision = "ADVANCE TO NEXT STAGE" if overall >= DECISION_THRESHOLD else "REJECT"
    print(f"Decision: {decision} (threshold {DECISION_THRESHOLD}%)\n")


def main():
    print("Job Applicant Scoring System\n----------------------------")
    while True:
        mode = input("Choose: (1) Enter applicant  (2) Quit : ").strip()
        if mode == "2":
            break
        if mode != "1":
            continue
        app = get_applicant_input()
        overall, components = compute_score(app)
        print_result(app, overall, components)


if __name__ == "__main__":
    main()