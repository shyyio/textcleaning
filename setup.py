from setuptools import setup

setup(
    name="textcleaning",
    version="4.2",
    description="Text cleaning",
    packages=["textcleaning"],
    install_requires=[
        "nltk",
        "lxml",
        "emoji",
        "unidecode"
    ]
)
