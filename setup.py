import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="dstructure", # Replace with your own username
    version="0.0.4",
    author="Vivek Pisal",
    author_email="vivekpisal12345@gmail.com",
    description="Data Structure",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["DS"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)



#python3 setup.py sdist bdist_wheel
#twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
