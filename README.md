# AutoRepInit

AutoRepInit is a Python script that simplifies the process of creating a new GitHub repository by utilizing the GitHub API. It accepts two command-line arguments: your GitHub personal access token and the desired repository name.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/alifertah/autoRepInit.git
   cd autoRepInit
   ```
   Run the script with your GitHub personal access token and repository name:
   ```bash
   python create_repo.py <your_token> <your_repository_name>
   ```
## Requirements

-   Python 3
-   Requests library (`pip install requests`)