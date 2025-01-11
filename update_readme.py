import requests
from bs4 import BeautifulSoup

# Dein GitHub-Benutzername
username = "LukiDev17"
repo_url = f"https://github.com/{username}"

def get_repos():
    response = requests.get(repo_url)
    soup = BeautifulSoup(response.content, "html.parser")
    repos = soup.find_all("a", {"itemprop": "name codeRepository"})
    repo_list = [repo.get_text(strip=True) for repo in repos]
    return repo_list

def update_readme(repos):
    with open("README.md", "w") as readme:
        readme.write(f"# 👋 Hi, I'm @{username}\n\n")
        readme.write("## 👀 Passionate about Private Servers\n\n")
        readme.write("### 🌱 Currently learning Python and Java\n\n")
        readme.write("#### 💞️ Open to collaboration on private server projects\n\n")
        readme.write(f"📫 Reach me on Telegram: @{username} or [Telegram](https://web.telegram.org/k/#@{username})\n\n")
        readme.write("<!-- First GIF -->\n")
        readme.write('<img src="https://media.giphy.com/media/xTiTnqUxyWbsAXq7Ju/giphy.gif" alt="Private Server GIF" style="display: block; margin-left: auto; margin-right: auto; width: 50%;"/>\n\n')
        readme.write("### 🚀 Latest Projects\n\n")
        for repo in repos:
            readme.write(f"- [{repo}](https://github.com/{username}/{repo})\n")

repos = get_repos()
update_readme(repos)
