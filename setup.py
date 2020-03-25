import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="slackhandler-bonartm", 
    version="0.0.1",
    author="Malte Bonart",
    author_email="malte@spiced-academy.com",
    description="A simple handler for the `logging` module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bonartm/slackhandler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests>=2']
)