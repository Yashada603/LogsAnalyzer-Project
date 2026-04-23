with open("logs.txt", "r") as file:
    for line in file:
        if "failed login" in line.lower():
            print("⚠️ Suspicious activity:", line.strip())