import datetime
import sys
from usefulFunc import Console, Files

db = "db.json"
log = open("LastLog.txt", "w")

project = []
Task = []

try:
    data = Files.jsonOpen(db)
    log.writelines(f"- {datetime.date.today()} : Successful open db\n")
except:
    log.write(f"- {datetime.date.today()} : Failed open db\n")

try:
    project = data.get("pr", [])
    Task = data.get("ex", [])
    log.write(f"- {datetime.date.today()} : Successful initialize project and Task\n")
except:
    log.write(f"- {datetime.date.today()} : Failed initialize project and Task\n")

print("----------------------------------------")
print("----------------- HI -------------------")
print("----------------------------------------")
print("\nActive project: ")
for p in project:
    print(" * " + p)

print("\nActive Task: ")
for e in Task:
    print(" * " + e)

print("\nDo you want to create/delete new project/Task(Y): ")
choose = input("=>").lower()
if choose != "y":
    sys.exit()
else:
    Console.clear()
    print("1. Create\n2. Delete")
    choose = input("=>")
    Console.clear()

    # Create operation
    if choose == "1":
        print("1. Project\n2. Task")
        choose = input("=>")
        name = input("Enter name: ")

        if choose == "1":
            project.append(name)
            log.write(f"- {datetime.date.today()} : Created new project {name}\n")
        elif choose == "2":
            Task.append(name)
            log.write(f"- {datetime.date.today()} : Created new Task {name}\n")
        else:
            sys.exit()

    elif choose == "2":
        print("1. Project\n2. Task")
        choose = input("=>")

        print("\nActive project: ")
        for p in project:
            print(" * " + p)

        print("\nActive Task: ")
        for e in Task:
            print(" * " + e)

        name = input("Enter name to delete: ")

        if choose == "1":
            if name in project:
                project.remove(name)
                log.write(f"- {datetime.date.today()} : Deleted project {name}\n")
            else:
                print(f"Error: {name} not found in project list.")
        elif choose == "2":
            if name in Task:
                Task.remove(name)
                log.write(f"- {datetime.date.today()} : Deleted Task {name}\n")
            else:
                print(f"Error: {name} not found in Task list.")
        else:
            sys.exit()

    else:
        sys.exit()

    data = {"pr": project, "ex": Task}
    Files.jsonOpen(db, 'w', data)

log.write("-------------------------------------------------------")
log.close()
