from setuptools import setup, find_packages

setup(
    name='gojyuuonjyunn',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pykakasi',
    ],
    author='Ryan Anderson',
    author_email='ryananderson0147@gmail.com',
    description='Simple Wrapper to Sort Japanese Strings in Gojyuuonjyunn Order',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Sakkyoku-Sha/gojyuuonjyunn',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)