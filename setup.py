import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyclibase",
    version="0.2.7",
    author="Sungkeun Kim",
    author_email="danguria@gmail.com",
    description = "A base class of python cli",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ksungkeun84/pyclibase",
    project_urls={
        "Bug Tracker": "https://github.com/ksungkeun84/pyclibase/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = [
        "setuptools>=42",
        "wheel",
        "rich",
        "pyfiglet"
    ],
)
