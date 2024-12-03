from git import Repo

repo_url = "https://github.com/hexs/auto_inspection_data_test.git"

clone_directory = r'C:\Users\EK\Desktop\New folder'
Repo.clone_from(repo_url, clone_directory)

print(f"Repository cloned to {clone_directory}")
