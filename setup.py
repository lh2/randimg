from setuptools import setup

import re
version_string = open('randimg/__init__.py', 'rt').read()
match = re.search(r'^__version__\s+=\s+[\'"](.*?)[\'"]$', version_string, re.M)
version = match.group(1)

setup(
    name='randimg',
    version=version,
    author='Lukas Henkel',
    author_email='lh@gehweg.org',
    url='https://github.com/lh2/randimg',
    license='MIT/X11',
    packages=['randimg'],
    entry_points={
        'console_scripts':[
            'randimg-qt = randimg.gui:main'
        ]
    }
)
