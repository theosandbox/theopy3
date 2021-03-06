from setuptools import setup

setup(
    name="theopy3",
    version="0.1",
    url="https://github.com/theosherry/theopy3",
    author="Theo Sherry",
    author_email="sherr.theo@gmail.com",
    license="MIT",
    packages=["theopy3", "theopy3.script_helpers"],
    install_requires=["colorama"],
    zip_safe=False)