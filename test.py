import requests
import sys
from requests.auth import HTTPBasicAuth
if len(sys.argv) != 3:
    print("WRONG ARGUMENTS")
elif len(sys.argv) == 3:
    token = sys.argv[1]
    repo_name = sys.argv[2]
    def create_repo(username, password, repo_name):
        url = "https://api.github.com/user/repos"
        data = {
            "name": repo_name,
            "auto_init": True       
        }

        response = requests.post(
            url,
            auth=HTTPBasicAuth(username, password),
            json=data
        )

        if response.status_code == 201:
            print(f"Repository '{repo_name}' created successfully!")
        else:
            print(f"Failed to create repository. Status code: {response.status_code}")
            print(response.text)

    if __name__ == "__main__":
        github_username = "alifertah"
        github_password = token
        repository_name = repo_name

        create_repo(github_username, github_password, repository_name)
