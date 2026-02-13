# test
import os

from github import Github


def get_pr_files_and_diff(repo_name: str, pr_number: int):

    token = os.getenv("GITHUB_TOKEN") or os.getenv("PR_AGENT_GITHUB_TOKEN")

    if not token:

        raise ValueError("Missing GitHub token")

    g = Github(token)

    repo = g.get_repo(repo_name)

    pr = repo.get_pull(pr_number)

    files = pr.get_files()

    diff_text = ""

    for file in files:

        diff_text += f"\nFile: {file.filename}\n"

        if file.patch:

            diff_text += file.patch + "\n"

    return files, diff_text
