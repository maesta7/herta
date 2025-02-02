from setuptools import setup, find_packages

setup(
    name='herta-core',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "pydantic"
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of your package',
    long_description=open('README.md').read(),  # Optional, for better documentation
    long_description_content_type='text/markdown',  # Optional, if using markdown
    url='https://github.com/yourusername/pck_name',  # Optional, your project URL
    classifiers=[  # Optional classifiers that help users find your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
