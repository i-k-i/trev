from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='treve',
    version='2017.02.22',
    description = 'Show translation of selected text',
    url='https://github.com/i-k-i/treve',
    author='i-k-i project',
    # author_email='',
    license='WTFPL',
    # packages=find_packages(),
    packages=['treve'],
    install_requires=[
        'PyQt5',
        'requests',
        'yandex.translate',
        'ipdb'
    ],
    # long_description=open(join(dirname(__file__), 'README.md')).read(),
    zip_safe=False,
    entry_points={
          'gui_scripts': [
              'treve = treve.gui:main'
          ]
      },
)
#🐍
