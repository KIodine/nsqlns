from setuptools import setup

from nsqlns import __version__ as mversion

setup(
    name="nsqlns",
    version=mversion,
    description="NoSQL namespace making routines.",
    author="KIodine",
    license="MIT",
    packages=['nsqlns']
)
