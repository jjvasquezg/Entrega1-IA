def show_week(best, DAYS):
    print("=== Weekly Plan ===")
    for d, act in zip(DAYS, best):
        print(f"{d:>3}: {act}")
    print("")

def summary(plan):
    counts = {"R": 0, "G": 0, "D": 0}
    for x in plan:
        counts[x] += 1
    print("Counter -> Run(R):", counts["R"], "| Gym(G):", counts["G"], "| Rest(D):", counts["D"])
