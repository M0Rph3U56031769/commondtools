import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commondtools",  # Replace with your own username
    version="0.0.6",
    author="Daniel Nagy",
    author_email="nagydaniel1337@gmail.com",
    description="Common tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M0Rph3U56031769/commondtools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
