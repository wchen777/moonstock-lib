from setuptools import find_packages, setup

setup(
    name='moonstock',
    packages=find_packages(),
    version='0.1.0',
    description='API for financial modeling and calculations.',
    author='Will Chen, Ankith Hiremath',
    license='MIT',
    install_requires=['numpy', 'scipy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
