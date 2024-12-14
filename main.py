import os
from random import randint

# Branchlarni yaratish
branches = ["branch1", "branch2"]

# Asosiy branchni tayyorlash
os.system("git checkout main")

# Branchlarni yaratish va commit qilish
for branch in branches:
    os.system(f"git checkout -b {branch}")
    for i in range(randint(1, 3)):  # Tasodifiy commitlar soni
        d = f'{i} days ago'
        with open('file.txt', 'a') as file:
            file.write(f'{branch} - commit {i}\n')
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "{branch} - commit {i}"')

# Main branchga qaytish
os.system("git checkout main")

# Branchlarni merge qilish
os.system(f"git merge {branches[0]}")
os.system(f"git merge {branches[1]}")

# O'zgarishlarni remote ga push qilish
os.system("git push -u origin main")

