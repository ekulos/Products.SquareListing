from setuptools import setup, find_packages
import os

version = '0.1.5'

setup(name='Products.SquareListing',
      version=version,
      description="A square listing template for folderish contents",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Plone Abstract browser vieww square listing',
      author='Luca Pisani',
      author_email='luca.pisani@abstract.it',
      url='htttp://www.abstract.it',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
