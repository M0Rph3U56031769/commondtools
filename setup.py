import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.0.25"

setuptools.setup(
    name="commondtools",
    version=version,
    author="Daniel Nagy",
    author_email="nagydaniel1337@gmail.com",
    description="Common D-tools.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/M0Rph3U56031769/commondtools",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        "astroid==2.4.2",
        "bleach==3.3.0",
        "bump2version==1.0.1",
        "bumpversion==0.6.0",
        "certifi==2020.12.5",
        "cffi==1.14.4",
        "chardet==3.0.4",
        "colorama==0.4.4",
        "coverage==5.3",
        "cryptography==3.3.2",
        "docutils==0.16",
        "idna>=2.5",
        "importlib-metadata==3.1.0",
        "isort==5.6.4",
        "jeepney==0.6.0",
        "keyring==21.5.0",
        "lazy-object-proxy==1.4.3",
        "mccabe==0.6.1",
        "numpy==1.19.4",
        "packaging==20.7",
        "pandas==1.1.4",
        "pkginfo==1.6.1",
        "pycparser==2.20",
        "Pygments~>2.7.4",
        "pylint==2.6.0",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pytz==2020.4",
        "pywin32-ctypes==0.2.0",
        "readme-renderer==28.0",
        "requests==2.25.0",
        "requests-toolbelt==0.9.1",
        "rfc3986==1.4.0",
        "SecretStorage==3.3.0",
        "selenium==3.141.0",
        "six==1.15.0",
        "toml==0.10.2",
        "tqdm==4.54.0",
        "twine==3.2.0",
        "urllib3~>1.26.5",
        "webencodings==0.5.1",
        "wrapt==1.12.1",
        "zipp==3.4.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
