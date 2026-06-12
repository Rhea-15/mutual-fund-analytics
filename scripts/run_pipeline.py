from pathlib import Path
import subprocess

scripts_dir = Path(__file__).parent

scripts = [
    "load_to_sqlite.py",
    "live_nav_fetch.py"
]

for script in scripts:
    script_path = scripts_dir / script

    if script_path.exists():
        subprocess.run(
            ["python", str(script_path)],
            check=True
        )
        print(f"{script} completed")
    else:
        print(f"{script} not found")

print("Pipeline executed successfully.")