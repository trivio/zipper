import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

README_PATH = os.path.join(HERE, 'README.md')
try:
    README = open(README_PATH).read()
except IOError:
    README = ''


setup(
  name='zipper',
  py_modules = ['zipper'],
  version='0.0.3',
  description=('Functional hierarchical zipper, with navigation, '
               'editing, and enumeration.  See Huet'),
  long_description=README,
  author='Scott Robertson',
  author_email='scott@triv.io',
  url='http://github.com/trivio/zipper',
  classifiers=[
      "Programming Language :: Python",
      "Programming Language :: Python :: 2",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.3",
      "Programming Language :: Python :: 3.4",
      "Programming Language :: Python :: 3.5",

      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Topic :: Software Development",
  ]
)
