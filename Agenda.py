from datetime import datetime

now = datetime.now()

print("Agenda Beatrice")
print(now.strftime("%A, %d.%m.%Y"))
print(now.strftime("%H:%M"))
