from setuptools import setup, find_packages
from whiteface import VERSION

with open('requirements.txt') as f:
    reqs = f.read().splitlines()


setup(
      name="whiteface-sdk",
      version=VERSION,
      description="WhiteFace Python SDK",
      long_description="WhiteFace Software Development Kit for Python",
      url="https://github.com/csirtgadgets/py-whiteface-sdk",
      license='LGPL3',
      classifiers=[
                   "Topic :: System :: Networking",
                   "Environment :: Other Environment",
                   "Intended Audience :: Developers",
                   "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
                   "Programming Language :: Python",
                   ],
      keywords=['security'],
      author="Wes Young",
      author_email="wes@barely3am.com",
      packages=find_packages(),
      install_requires=reqs,
      scripts=['bin/wf'],
      test_suite="test"
)
