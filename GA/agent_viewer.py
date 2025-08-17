import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.dirname(__file__))  # .../ga_training_plan_project
GA_DIR = os.path.join(BASE_DIR, "GA")
if GA_DIR not in sys.path:
    sys.path.insert(0, GA_DIR)

from ga_training import DAYS, fitness, is_valid 

def load_best():
    path = os.path.join(BASE_DIR, "imgs", "best_plan.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def show_week(plan):
    print("=== Plan semanal ===")
    for d, act in zip(DAYS, plan):
        print(f"{d:>3}: {act}")
    print("")

def summary(plan):
    counts = {"R": 0, "G": 0, "D": 0}
    for x in plan:
        counts[x] += 1
    print("Conteo -> Correr(R):", counts["R"], "| Gimnasio(G):", counts["G"], "| Descanso(D):", counts["D"])

if __name__ == "__main__":
    data = load_best()
    plan = data["best_plan"]
    show_week(plan)
    print("Válido:", is_valid(plan))
    print("Fitness:", fitness(plan))
    summary(plan)
