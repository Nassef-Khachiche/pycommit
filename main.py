import os
import subprocess
import random
import datetime

# Set the repository path (modify if needed)
repo_path = os.getcwd()

# Ensure it's a Git repository
if not os.path.isdir(os.path.join(repo_path, ".git")):
    print("Error: This is not a Git repository.")
    exit(1)

# Generate commit dates from 1970 to January 2025
start_year = 1970
end_year = 2025
commit_count = 100  # Number of commits

for _ in range(commit_count):
    # Generate a random date
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Keeping it safe for February
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)

    commit_date = datetime.datetime(year, month, day, hour, minute, second)
    commit_date_str = commit_date.strftime("%Y-%m-%d %H:%M:%S")

    # Set environment variable for commit date
    env = os.environ.copy()
    env["GIT_COMMITTER_DATE"] = commit_date_str

    # Make a dummy commit
    with open(os.path.join(repo_path, "dummy_file.txt"), "a") as f:
        f.write(f"Commit on {commit_date_str}\n")

    subprocess.run(["git", "add", "dummy_file.txt"], cwd=repo_path)
    subprocess.run(["git", "commit", "-m", f"Commit on {commit_date_str}", "--date", commit_date_str], cwd=repo_path, env=env)

    print(f"Committed on {commit_date_str}")

print("All commits generated successfully!")