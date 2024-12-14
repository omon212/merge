import os

# Konfiguratsiya
MAIN_BRANCH = "main"
DETACHED_BRANCH = "detached"
FILE_NAME = "file.txt"

# Git komandalarini bajaruvchi funksiya
def run_command(command):
    print(f"Running: {command}")
    os.system(command)

# 1. Main branchdagi o'zgarishlarni olish va fayl yaratish
print("\n--- Switching to main branch ---")
run_command(f"git checkout {MAIN_BRANCH}")
run_command(f"git pull origin {MAIN_BRANCH}")

print("Creating and writing to file in main branch...")
with open(FILE_NAME, "w") as f:
    f.write("Bu main branch uchun fayl.\n")

run_command(f"git add {FILE_NAME}")
run_command(f'git commit -m "Main branch: {FILE_NAME} yaratildi va to\'ldirildi"')
run_command(f"git push origin {MAIN_BRANCH}")

# 2. Detached branchdagi o'zgarishlarni olish va fayl yaratish
print("\n--- Switching to detached branch ---")
run_command(f"git checkout {DETACHED_BRANCH}")
run_command(f"git pull origin {DETACHED_BRANCH}")

print("Creating and writing to file in detached branch...")
with open(FILE_NAME, "w") as f:
    f.write("Bu detached branch uchun fayl.\n")

run_command(f"git add {FILE_NAME}")
run_command(f'git commit -m "Detached branch: {FILE_NAME} yaratildi va to\'ldirildi"')
run_command(f"git push origin {DETACHED_BRANCH}")

# 3. Main branchga qaytish va merge qilish
print("\n--- Merging detached branch into main branch ---")
run_command(f"git checkout {MAIN_BRANCH}")
run_command(f"git merge {DETACHED_BRANCH}")

# Merge natijasini push qilish
print("Pushing merged changes to main branch...")
run_command(f"git push origin {MAIN_BRANCH}")

print("\nDone! File created and merged successfully.")

