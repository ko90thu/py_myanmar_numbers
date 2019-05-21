import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='py_myanmar_numbers_pkg',
     version='1.0.1',
     author="ko90thu",
     author_email="ko90thu@gmail.com",
     description="Convert Myanmar Numbers to English Numbers",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/ko90thu/py_myanmar_numbers",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
