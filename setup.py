from setuptools import setup

setup(
    name='weatherpredict',
    author="Mszanowski Dawid, Jokisz Adrian",
    version='0.1.0',
    description="CLI tool for weather prediction using machine learning models.",
    py_modules=['weatherpredict'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'weatherpredict = app:cli',
        ],
    },
)
