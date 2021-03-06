import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vsimcon",
    version="0.0.1",
    author="Timothy Mc Alister",
    author_email="timothy@mcalister.ch",
    description="A simple package to simulate and control flow between interconnected vessels",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tsmcalister/vsimcon",
    packages=setuptools.find_packages(exclude=("tests",)),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["numpy", "matplotlib"],
    python_requires='>=3.6',
)
