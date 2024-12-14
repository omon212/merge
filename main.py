import os

# 100 ta branch yaratib merge qilish uchun funksiya
def automated_commits():
    # main branchga o'tish
    os.system("git checkout main")

    for i in range(1, 101):  # 100 ta branch loop
        branch_name = f"auto-branch-{i}"

        # Yangi branch yaratish
        os.system(f"git checkout -b {branch_name}")

        # Faylga o'zgartirish kiritish
        with open("file.txt", "a") as file:
            file.write(f"Branch {branch_name} commit\n")

        # Commit qilish
        os.system("git add file.txt")
        os.system(f"git commit -m 'Commit from {branch_name}'")

        # main branchga qaytib merge qilish
        os.system("git checkout main")
        os.system(f"git merge --no-ff {branch_name} -m 'Merge {branch_name} into main'")

        # Branchni o'chirib yuborish (ixtiyoriy)
        os.system(f"git branch -d {branch_name}")

    # Oxirgi commitlarni remote repositoryga push qilish
    os.system("git push origin main")

if __name__ == "__main__":
    automated_commits()

