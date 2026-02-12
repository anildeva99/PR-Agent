
import os
from utils.github_client import get_pr_files_and_diff
from utils.teams_client import send_teams_message

def main():
    print("🚀 Starting PR Agent")

    repo_name = os.getenv("PR_AGENT_REPO")
    pr_number = os.getenv("PR_NUMBER")

    if not repo_name or not pr_number:
        raise ValueError("PR_AGENT_REPO or PR_NUMBER missing")

    pr_number = int(pr_number)

    print(f"�� Repository : {repo_name}")
    print(f"🔢 PR Number  : {pr_number}")

    # Get PR files & diff
    files, diff = get_pr_files_and_diff(repo_name, pr_number)

    #files_count = len(files)
    files = list(files)
    files_count = len(files)
    diff_length = len(diff)

    print(f"📂 Files changed : {files_count}")
    print(f"📏 Diff length  : {diff_length}")

    # Slack notification
    teams_message = (
        f"🔍 PR Review Completed\n"
        f"Repository: {repo_name}\n"
        f"PR Number: #{pr_number}\n"
        f"Files Changed: {files_count}\n"
        f"Diff Length: {diff_length}"
    )

    send_teams_message(teams_message)

    # Optional AI Review (safe)
    if os.getenv("GOOGLE_API_KEY"):
        try:
            from utils.ai_reviewer import run_ai_review
            run_ai_review(diff)
            send_teams_message("🤖 AI Review completed successfully.")
        except Exception as e:
            send_teams_message(f"❌ AI Review failed: {e}")
    else:
        send_teams_message("⚠️ GOOGLE_API_KEY not set. Skipping AI review.")

if __name__ == "__main__":
    main()

