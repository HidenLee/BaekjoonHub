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

def get_newly_added_files():
    try:
        result = subprocess.check_output(
            ['git', 'diff', '--name-only', 'HEAD~1', 'HEAD'],
            universal_newlines=True
        )
        return [line.strip() for line in result.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        print("Error detecting new files:", e)
        return []

def send_discord_notification(title, file_path):
    if not DISCORD_WEBHOOK_URL:
        print("No Discord webhook URL found.")
        return
    
    print(f"[DISCORD] Sending title: {title}, file_path: {file_path}")
    
    # Try to extract problem ID from filename
    base = os.path.basename(file_path)
    problem_id = base.split('.')[0]
    if problem_id.isdigit():
        url = f"https://www.acmicpc.net/problem/{problem_id}"
    else:
        url = f"https://github.com/{os.environ.get('GITHUB_REPOSITORY')}/blob/{os.environ.get('GITHUB_SHA')}/{file_path}"

    payload = {
        "username": "BaekjoonHub Bot",
        "embeds": [{
            "title": title,
            "url": url,
            "description": f"🆕 새로운 문제 풀이가 업로드되었습니다.",
            "type": "link"
        }]
    }

    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        print("Discord response:", response.status_code)
    except Exception as e:
        print("Failed to send webhook:", e)

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

    with open("README.md", "w") as fd:
        fd.write(content)

    # If BaekjoonHub title is set, find the newly added file and notify
    if PROBLEM_TITLE:
        added_files = get_newly_added_files()
        for file in added_files:
            if file.endswith(('.py', '.cpp', '.js')) and '백준' in file:
                send_discord_notification(PROBLEM_TITLE, file)
                break

if __name__ == "__main__":
    main()
