#!/usr/bin/env python3
from typing import Dict, List
import random

class Expense:
    def __init__(self, category: str, amount: float):
        self.category = category
        self.amount = amount

class BudgetPlanner:
    def __init__(self, budget: Dict[str, float]):
        self.budget = budget  # {"Food": 300, "Rent": 800, "Entertainment": 150}
        self.expenses: List[Expense] = []

    def add_expense(self, category: str, amount: float):
        if category not in self.budget:
            raise ValueError("Category not in budget")
        self.expenses.append(Expense(category, amount))

    def category_expenses(self) -> Dict[str, float]:
        totals: Dict[str, float] = {cat: 0 for cat in self.budget}
        for e in self.expenses:
            totals[e.category] += e.amount
        return totals

    def budget_utilization(self) -> Dict[str, float]:
        totals = self.category_expenses()
        return {cat: round((totals[cat] / self.budget[cat]) * 100, 2) for cat in self.budget}

    def overall_summary(self) -> Dict[str, float]:
        spent = sum(e.amount for e in self.expenses)
        allocated = sum(self.budget.values())
        return {
            "Total Budget": allocated,
            "Total Spent": spent,
            "Remaining": allocated - spent,
            "Utilization %": round((spent / allocated) * 100, 2) if allocated > 0 else 0
        }

def demo():
    budget = {"Food": 300, "Rent": 800, "Entertainment": 150, "Transport": 100}
    planner = BudgetPlanner(budget)

    # Generate random expenses
    categories = list(budget.keys())
    for _ in range(20):
        planner.add_expense(random.choice(categories), random.uniform(5, 100))

    print("Category Expenses:", planner.category_expenses())
    print("Budget Utilization (%):", planner.budget_utilization())
    print("Overall Summary:", planner.overall_summary())

if __name__ == "__main__":
    demo()
