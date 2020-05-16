import os
from setuptools import setup

ABOUT = {}

with open(os.path.join(os.path.dirname(__file__), 'agrafena', '__about__.py')) as file:
    exec(file.read(), ABOUT)

LONG_DESCRIPTION = """# agrafena

Python TN3270 automation library.

See [GitHub](https://github.com/lowobservable/agrafena#readme) for more information.
"""

setup(
    name='agrafena',
    version=ABOUT['__version__'],
    description='TN3270 automation library',
    url='https://github.com/lowobservable/agrafena',
    author='Andrew Kay',
    author_email='projects@ajk.me',
    packages=['agrafena'],
    install_requires=['pytn3270==0.5.0'],
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Communications',
        'Topic :: Terminals',
        'Topic :: Software Development :: Testing'
    ]
)
