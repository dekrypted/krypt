
  
from setuptools import setup, find_packages

__name__ = "krypt"
__version__ = "0.0.1"

setup(
    name=__name__,
    version=__version__,
    author="DeKrypt",
    author_email="no",
    description="My library which includes windows functions, discord functions, common functions, and more!",
    long_description_content_type="text/markdown",
    long_description=open("README.md", encoding="utf-8").read(),
    url = "https://github.com/dekrypted/krypt",
    project_urls={
      "Bug Tracker": "https://github.com/dekrypted/krypt/issues",
    },
    install_requires=['requests'],
    packages=find_packages(),
    keywords=['krypt','discord'],
    classifiers=[
      "Intended Audience :: Developers",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
    ]
)
