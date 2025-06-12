from setuptools import setup
from bython import VERSION_NUMBER

with open("README.md", "r") as fh:
    long_description = fh.read()

# Install python package, scripts and manual pages
setup(name="sbd",
      version=VERSION_NUMBER,
      author="Salah Rami Al-Refaai",
      author_email="salah.alrerae@gmail.com",
      license="MIT",
      description="SBD (Salah's Bython Distribution)",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/Salah2PLS/SBD-Bython.git",
      scripts=["scripts/bython"],
      packages=["bython"],
      zip_safe=False)