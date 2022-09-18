from setuptools import setup

setup(
    name='flask_blog',
    version='0.1.0',
    packages=['blog'],
    install_requires=[
        'dynaconf',
        'flask',
        'flask-bootstrap',
        'flask-pymongo',
        'flask-shell-ipython',
        'ipdb',
        'mistune',
        'python-slugify',
        'flask-simplelogin',
    ]
)
