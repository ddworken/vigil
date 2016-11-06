from distutils.core import setup

setup(
    name='vigil',
    version='0.1',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['vigil'],
    url='http://pypi.python.org/pypi/vigil/',
    license='LICENSE.txt',
    description='vigil... as a python package',
    long_description=open('README.rd').read(),
    install_requires=[
        "sys",
        "operators",
        "inspect",
    ],
)
