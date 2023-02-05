from pathlib import Path #mayuskulak klase bat dela esan nahi du

path = Path()

for file in path.glob("*.py"):
    print(file)