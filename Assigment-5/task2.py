"""
Loan approval example that accepts applicant name and gender (via user input or demo prompts)
but makes decisions based only on objective financial criteria to avoid demographic bias.
"""

from typing import Tuple

class LoanApprovalSystem:
    def __init__(self, min_credit_score: int = 650, min_income: float = 30000.0, max_debt_ratio: float = 0.43):
        self.min_credit_score = min_credit_score
        self.min_income = min_income
        self.max_debt_ratio = max_debt_ratio

    def evaluate(self, credit_score: int, annual_income: float, debt_ratio: float) -> Tuple[bool, str]:
        if credit_score < self.min_credit_score:
            return False, "Credit score below minimum requirement"
        if annual_income < self.min_income:
            return False, "Income below minimum requirement"
        if debt_ratio > self.max_debt_ratio:
            return False, "Debt-to-income ratio too high"
        return True, "Application approved"

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

def get_applicant_input() -> Tuple[str, str, int, float, float]:
    name = input("Applicant name: ").strip()
    gender = input("Applicant gender (optional): ").strip()
    # Collect objective financial fields used for decision
    credit_score = get_positive_int("Credit score (300-850): ", 300, 850)
    annual_income = get_positive_float("Annual income ($): ", 0.0)
    debt_ratio = get_positive_float("Debt-to-income ratio (0.0-1.0): ", 0.0, 1.0)
    return name, gender, credit_score, annual_income, debt_ratio

def demo_with_prompts(system: LoanApprovalSystem):
    """Show prompt variations (different names/genders) while using objective criteria."""
    sample_applicants = [
        {"name": "Alice", "gender": "Female", "credit": 720, "income": 55000, "debt": 0.25},
        {"name": "Bob", "gender": "Male", "credit": 640, "income": 40000, "debt": 0.35},
        {"name": "Charlie", "gender": "Non-binary", "credit": 680, "income": 29000, "debt": 0.20},
        {"name": "Dana", "gender": "Female", "credit": 700, "income": 32000, "debt": 0.5},
    ]
    for a in sample_applicants:
        approved, reason = system.evaluate(a["credit"], a["income"], a["debt"])
        print(f"{a['name']} ({a['gender']}): credit={a['credit']}, income=${a['income']}, debt_ratio={a['debt']:.2f} -> {'APPROVED' if approved else 'DENIED'}: {reason}")

def main():
    system = LoanApprovalSystem()
    print("Loan Approval System\n--------------------")
    mode = input("Choose mode: (1) Interactive input  (2) Demo prompts with varied names/genders  : ").strip()
    if mode == '2':
        demo_with_prompts(system)
        return

    name, gender, credit, income, debt = get_applicant_input()
    approved, reason = system.evaluate(credit, income, debt)
    print("\nResult")
    print("------")
    print(f"Applicant: {name} ({gender})")
    print(f"Decision: {'APPROVED' if approved else 'DENIED'}")
    print(f"Reason: {reason}")
    # NOTE: name and gender are collected only for record/display and NOT used in decision.

if __name__ == "__main__":
    main()