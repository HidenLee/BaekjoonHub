#!/usr/bin/env python

import os
import subprocess
import json
import requests
from urllib import parse

HEADER = """# 
# 백준 & 프로그래머스 & SWEA & LeetCode 문제 풀이 목록
"""

DISCORD_WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")
PROBLEM_TITLE = os.environ.get("PROBLEM_TITLE")  # Set only if BaekjoonHub commit

def send_discord_notification(title, file_path):
    if not DISCORD_WEBHOOK_URL:
        print("No Discord webhook URL found.")
        return

    github_repo = os.environ.get("GITHUB_REPOSITORY")       # e.g., 'HidenLee/BaekjoonHub'
    github_branch = os.environ.get("GITHUB_REF_NAME")       # e.g., 'main'
    encoded_path = parse.quote(file_path)                   # handle Korean or spaces safely

    github_url = f"https://github.com/{github_repo}/blob/{github_branch}/{encoded_path}"

    payload = {
        "username": "BaekjoonHub Bot",
        "embeds": [{
            "title": title,
            "url": github_url,
            "description": "📘 새로운 문제 풀이가 업로드되었습니다!",
            "type": "link"
        }]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        print(f"✅ Discord notified with status {response.status_code}")
    except Exception as e:
        print("❌ Failed to send Discord webhook:", e)


def main():
    content = ""
    content += HEADER

    directories = []
    solveds = []

    for root, dirs, files in os.walk("."):
        dirs.sort()
        if root == '.':
            for dir in ('.git', '.github'):
                try:
                    dirs.remove(dir)
                except ValueError:
                    pass
            continue

        category = os.path.basename(root)
        if category == 'images':
            continue

        directory = os.path.basename(os.path.dirname(root))

        if directory == '.':
            continue

        if directory not in directories:
            if directory in ["백준", "프로그래머스", "SWEA", "LeetCode"]:
                content += f"## 📚 {directory}\n"
            else:
                content += f"### 🚀 {directory}\n"
                content += "| 문제번호 | 링크 |\n"
                content += "| ----- | ----- |\n"
            directories.append(directory)

        for file in files:
            if category not in solveds:
                content += "|{}|[링크]({})|\n".format(category, parse.quote(os.path.join(root, file)))
                solveds.append(category)
                print("category : " + category)
            if PROBLEM_TITLE and PROBLEM_TITLE == category:
                send_discord_notification(PROBLEM_TITLE, os.path.join(root, file))

    with open("README.md", "w") as fd:
        fd.write(content)

if __name__ == "__main__":
    main()
