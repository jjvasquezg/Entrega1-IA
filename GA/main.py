# main.py
import subprocess, sys, os

def run_script(script_path):
    print(f"\n=== Ejecutando {os.path.relpath(script_path)} ===\n")
    result = subprocess.run([sys.executable, script_path], cwd=os.path.dirname(script_path))
    if result.returncode != 0:
        raise RuntimeError(f"Error ejecutando {script_path}")

if __name__ == "__main__":
    base = os.path.dirname(__file__)

    # 1) Ejecutar GA (genera /imgs/best_plan.json y /imgs/fitness_history.csv)
    run_script(os.path.join(base, "GA", "ga_training.py"))

    # 2) Mostrar resultados con el agente (imprime en consola)
    run_script(os.path.join(base, "Agent", "agent_viewer.py"))

    print("\n=== Flujo completo terminado con éxito ===")