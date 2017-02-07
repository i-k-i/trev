from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='trev',
    version='2017.02.07',
    description = 'Show translation of selected text',
    url='https://github.com/i-k-i/trev',
    author='i-k-i project',
    # author_email='',
    license='WTFPL',
    # packages=find_packages(),
    packages=['trev'],
    install_requires=[
        'PyQt5'
    ],
    long_description=open(join(dirname(__file__), 'trev', 'README.md')).read(),
    zip_safe=False,
    entry_points={
          'gui_scripts': [
              'trev = trev.gui:main'
          ]
      },
)
#🐍
