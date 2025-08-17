def show_week(best, DAYS):
    print("=== Plan semanal ===")
    for d, act in zip(DAYS, best):
        print(f"{d:>3}: {act}")
    print("")

def summary(plan):
    counts = {"R": 0, "G": 0, "D": 0}
    for x in plan:
        counts[x] += 1
    print("Conteo -> Correr(R):", counts["R"], "| Gimnasio(G):", counts["G"], "| Descanso(D):", counts["D"])
