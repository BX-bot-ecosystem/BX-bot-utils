from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    description = fh.read()

with open("requirements.txt", 'r') as fh:
    requirements = [l.strip() for l in fh.readlines()]
print(requirements)

setup(
    name="bx-utils",
    version='0.4',
    author="BX-bot-ecosystem",
    author_email="something@something.something",
    packages=find_packages(),
    description="Utilites for BX bots",
    long_description=description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    python_requires='>=3.8',
    install_requires=requirements, 
)
