from setuptools import find_packages,setup


def get_requirements():
    


setup(
    name='sensor',
    version= '0.0.1' ,
    author= 'Amrit Raj',
    author_email= 'amrit224raj@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements(),

)