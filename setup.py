from setuptools import setup, find_packages

setup(
    name='kempelenai_core',
    version='0.0.1',
    description='Kempelen AI Core App',
    author='DasKapital One',
    author_email='claudio.roman@daskapital.one',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=['frappe'],
)
