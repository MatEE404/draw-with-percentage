from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='draw with percentage',
      version='0.0.6',
      description='Python Library to draw with percentage',
      long_description=long_description,
      url="https://github.com/MatEE404/draw-with-percentage",
      long_description_content_type='text/markdown',
      author='Mateusz Kołodziejczyk',
      author_email='mateusz.j.kolodziejczyk@gmail.com',
      license='MIT',
      python_requires='>=3',
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.8',
          "License :: OSI Approved :: MIT License",
          'Operating System :: OS Independent'
      ],
      packages=find_packages()
      )
