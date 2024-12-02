from setuptools import setup, find_packages

setup(
    name="testcaseManager",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "rich"
    ],
    author="Sting Zhang",
    author_email="Stingzhang9000@gmail.com",
    description="A script that will detect in and out files from the directory and read them as string and compare output of a given function",
)