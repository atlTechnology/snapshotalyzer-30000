from setuptools import setup

setup(
    name='snapshotalyzer-30000',
    version='0.1',
    author="ATL",
    author_email="trade2308@outlook.com",
    description="SnapshotAlyzer 30000 is a toll to manage AWS EC2 snapshots",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/atlTechnology/snapshotalyzer-30000",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
