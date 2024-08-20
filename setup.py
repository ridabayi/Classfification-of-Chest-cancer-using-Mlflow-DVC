import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

repo_name = "Chest_Cancer_Classification-Project"
author_user_name = "ridabayi"
src_repo = "cnnClassifier"
author_email = "bayi.rida@gmail.com"

setuptools.setup(name = src_repo,
                 version=__version__,
                 author=author_user_name,
                 author_email=author_email,
                 description="a small python package for CNN app",
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url=f"https://github.com/{author_user_name}/{repo_name}",
                 project_urls={
                 "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",},
                 package_dir={"": "src"},
                 packages=setuptools.find_packages(where="src"))