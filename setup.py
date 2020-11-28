import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="commondtools",
    version="0.0.11",
    author="Daniel Nagy",
    author_email="nagydaniel1337@gmail.com",
    description="Common D-tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M0Rph3U56031769/commondtools",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=["sys", "socket", "subprocess", "multiprocessing"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
