with open("sho_is_this", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("work", "w", encoding="utf-8") as f:
    for line in lines:
        if line.strip():
            f.write(line)