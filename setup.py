import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="meishiki",
    version="0.1.0",
    author="tk42",
    author_email="nsplat+pip@gmail.com",
    description="Calculation of Four Pillars of Destiny",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.7",
    install_requires=[
        "jinja2 >= 2.11.2",
        "pyyaml >= 5.3.1",
        "python-box >= 5.2.0",
    ],
)
