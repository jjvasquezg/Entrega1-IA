import random
import json
import csv
import os
import time
from typing import List
from UtilGA import show_week, summary

# --- Datos del problema ---
# 7 días: genes con valores 'R' (correr), 'G' (gimnasio), 'D' (descanso)
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
GENES = ['R', 'G', 'D']

def is_valid(plan: List[str]) -> bool:
    # Condiciones "duras" mínimas: al menos 2 R y 2 G, no más de 3 entrenos seguidos
    r = plan.count('R')
    g = plan.count('G')

    consec_train = 0
    for x in plan:
        if x in ('R', 'G'):
            consec_train += 1
            if consec_train > 3:
                return False
        else:
            consec_train = 0

    if r < 2 or g < 2:
        return False
    return True

def fitness(plan: List[str]) -> float:
    # Puntuación base
    score = 100.0

    # 1) Penalizar más de 3 entrenos seguidos
    consec_train = 0
    extra_pen = 0.0
    for x in plan:
        if x in ('R', 'G'):
            consec_train += 1
            if consec_train > 3:
                extra_pen += 5.0  # penalización por cada extra consecutivo
        else:
            consec_train = 0
    score -= extra_pen

    # 2) Mínimos de volumen: al menos 2 R y 2 G
    r = plan.count('R')
    g = plan.count('G')
    if r < 2:
        score -= (2 - r) * 12.0
    if g < 2:
        score -= (2 - g) * 12.0

    # 3) Evitar demasiado descanso (más de 3 D)
    d = plan.count('D')
    if d > 3:
        score -= (d - 3) * 4.0

    # 4) Pequeño bono por alternancia (transiciones entre tipos diferentes)
    transitions = sum(1 for i in range(1, len(plan)) if plan[i] != plan[i-1])
    score += 0.5 * transitions

    # 5) Bono por descanso estratégico después de 2–3 entrenos seguidos
    consec = 0
    strategic_bonus = 0.0
    for x in plan:
        if x in ('R', 'G'):
            consec += 1
        else:
            if consec in (2, 3):
                strategic_bonus += 2.0
            consec = 0
    score += strategic_bonus

    return score

# --- Generación de población ---
def create_individual() -> List[str]:
    return [random.choice(GENES) for _ in range(len(DAYS))]

def create_population(size: int = 40) -> List[List[str]]:
    return [create_individual() for _ in range(size)]

# --- Operadores GA: selección, cruce, mutación ---
def selection(population: List[List[str]]) -> List[str]:
    # Torneo de 2 (como el profe)
    a, b = random.sample(population, 2)
    return a if fitness(a) > fitness(b) else b

def crossover(p1: List[str], p2: List[str]) -> List[str]:
    # Segmento de p1 y relleno con p2 (esquema del profe; válido con genes repetibles)
    size = len(p1)
    start, end = sorted(random.sample(range(size), 2))
    child = [None] * size
    child[start:end] = p1[start:end]
    idx = 0
    for i in range(size):
        if child[i] is None:
            child[i] = p2[idx]
            idx += 1
    return child

def mutate(ind: List[str], prob: float = 0.2) -> List[str]:
    if random.random() < prob:
        i, j = random.sample(range(len(ind)), 2)
        ind[i], ind[j] = ind[j], ind[i]
    return ind

# --- Evolución ---
def evolve(population: List[List[str]], generations: int = 30):
    text = '=========================== PRINTING GENERATIONS ==========================='
    print(text.center(20))
    history = []  # (gen, best_f, avg_f)
    best = max(population, key=fitness)
    for gen in range(generations):
        new_pop = []
        for _ in range(len(population)):
            p1 = selection(population)
            p2 = selection(population)
            child = crossover(p1, p2)
            child = mutate(child)
            new_pop.append(child)
        population = new_pop
        best = max(population, key=fitness)
        avg = sum(fitness(ind) for ind in population) / len(population)
        history.append((gen+1, fitness(best), avg))
        print(f"Gen {gen+1:2d}: {best} | Fitness: {fitness(best):.2f} | Válido: {is_valid(best)}")
    return best, history

def save_results(best, history, out_dir="../imgs/GA_imgs"):
    # Ruta robusta y creación de carpeta automáticamente
    base_dir = os.path.dirname(__file__)               # .../GA
    out_dir = os.path.abspath(os.path.join(base_dir, "..", "imgs","GA_imgs"))
    os.makedirs(out_dir, exist_ok=True)

    result = {
        "days": DAYS,
        "genes": GENES,
        "best_plan": best,
        "fitness": fitness(best),
        "valid": is_valid(best)
    }
    with open(os.path.join(out_dir, "best_plan.json"), "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    with open(os.path.join(out_dir, "fitness_history.csv"), "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["generation", "best", "average"])
        for g, b, a in history:
            writer.writerow([g, b, a])

initial = time.perf_counter()
random.seed(7)
pop = create_population(size=40)
best, hist = evolve(pop, generations=30)
total = time.perf_counter() - initial
print("\nBest plan found:", best)
print(f"This solution was found in: {(total)*1000:.8f} milliseconds", "\n")

save_results(best, hist)
show_week(best, DAYS)
print("Valid:", is_valid(best))
print("Fitness:", fitness(best))
summary(best)