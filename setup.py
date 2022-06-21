from setuptools import setup, find_packages

PKG_NAME = "torchtest_shaliulab"
version = "0.0.1"

with open(f"{PKG_NAME}/__init__.py", "w") as fh:
    fh.write(f"__version__ = '{version}'\n")

setup(
    name=PKG_NAME,
    version=version,
    packages = find_packages(),
    extras_require={
    },
    install_requires=[
        "torch", "numpy"
    ],
    entry_points={
        "console_scripts": [
            "torchtest=torchtest.torchtest:main",
            ]
    },
)



