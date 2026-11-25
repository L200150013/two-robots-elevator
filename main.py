import os

# Two Robots in an Elevator — one robot overthinks saying hello, 116 chars (Fable's pick), to /output/entry.txt
LINE = "I ran 14 simulations of saying hello in this elevator. Every single one ended with me saying hello like that. Hello."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
