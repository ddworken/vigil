from distutils.core import setup
import pypandoc

setup(
    name='vigil',
    version='0.1.2',
    author='David Dworken',
    author_email='david@daviddworken.com',
    packages=['vigil'],
    url='http://pypi.python.org/pypi/vigil/',
    license='LICENSE.txt',
    description='vigil... as a python package',
    long_description=pypandoc.convert("README.md", "rst"),
)
