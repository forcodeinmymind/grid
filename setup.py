from setuptools import find_packages, setup


setup(
    name='grid',
    version='1.0',
    packages=find_packages(),
    install_requires=[],
    include_package_data=True,
    description='Cartesian coordinate system class `Grid`',
    author='Michael Naef',
    author_email='mister_naef@hotmail.com',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)
