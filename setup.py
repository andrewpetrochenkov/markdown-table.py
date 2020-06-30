import setuptools

setuptools.setup(
    name='markdown-table',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
