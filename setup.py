from setuptools import setup

setup(
    name="textcleaning",
    version="6.0",
    description="Text cleaning",
    packages=["textcleaning"],
    install_requires=[
        "nltk",
        "lxml",
        "emoji",
        "unidecode"
    ]
)
