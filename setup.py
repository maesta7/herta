from setuptools import setup, find_packages

setup(
    name='herta-core',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "pydantic"
    ],
    author='Pon Pongwachirin',
    author_email='tar.workspace@gmail.com',
    description='Core LLM Package',
    #long_description=open('README.md').read(),
    #long_description_content_type='text/markdown',
    url='https://github.com/maesta7/herta',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
