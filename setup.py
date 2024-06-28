from setuptools import setup, find_packages

setup(
    name='automation',
    version='1.0.0',
    packages=find_packages(),
    description='Pacote para acelerar desenvolvimento de automações com selenium.',
    author='Mateus Herrera Gobetti Borges',
    author_email='mateusherreragb05@gmail.com',
    url='https://github.com/mateusherrera/basic_selenium',
    install_requires=['selenium', 'webdriver-manager'],
)
