import requests

ORG_NAME = "BAMresearch"
API_URL = f"https://api.github.com/orgs/{ORG_NAME}/repos"
PER_PAGE = 50

README_PATH = "README.md"
SECTION_MARKER_START = "## List of repositories"
SECTION_MARKER_END = "## License"


def fetch_all_repos():
    repos = []
    page = 1
    while True:
        url = f"{API_URL}?per_page={PER_PAGE}&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            raise RuntimeError(f"GitHub API error: {response.status_code} – {response.text}")
        data = response.json()
        if not data:
            break
        repos.extend(data)
        page += 1
    return repos


def format_repo_list(repos):
    # Sort alphabetically
    repos.sort(key=lambda x: x["name"].lower())
    lines = []
    for repo in repos:
        if repo.get("private", False):
            continue
        name = repo.get("name")
        if not name:
            continue
        if name in [".codemeta", ".github", ".oss", ".oss-strategy"]
        desc = repo.get("description", "")
        url = repo.get("html_url", "https://github.com/BAMresearch")
        if desc:
            lines.append(f"- [{name}]({url}) – {desc}")
        else:
            lines.append(f"- [{name}]({url})")
    return "\n".join(lines)

- [.codemeta](https://github.com/BAMresearch/.codemeta) – BAM CodeMeta Guidelines
- [.github](https://github.com/BAMresearch/.github) – None
- [.oss](https://github.com/BAMresearch/.oss) – Introduction and self-commitment of BAM
- [.oss-strategy]
def update_readme(formatted_repos):
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if SECTION_MARKER_START not in content or SECTION_MARKER_END not in content:
        raise ValueError("README missing required section markers.")

    before = content.split(SECTION_MARKER_START)[0].rstrip()
    after = content.split(SECTION_MARKER_END)[1].lstrip()

    new_section = f"{SECTION_MARKER_START}\n\n{formatted_repos}\n\n{SECTION_MARKER_END}"
    new_content = f"{before}\n\n{new_section}\n\n{after}"

    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)


def main():
    repos = fetch_all_repos()
    formatted = format_repo_list(repos)
    update_readme(formatted)


if __name__ == "__main__":
    main()
