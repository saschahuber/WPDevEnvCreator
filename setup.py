import setuptools

setuptools.setup(
    name="WPDevEnvCreator",
    version="%%WP_DEV_ENV_CREATOR_VERSION_NUMBER%%",
    author="Sascha Huber",
    author_email="kontakt@sascha-huber.com",
    description="Create dev-environments of your Wordpress-Site with ease!",
    long_descritpion="DevEnv-Creator-Tool for Wordpress",
    long_description_content_type="text/markdown",
    url="https://github.com/dersaschahuber/WPDevEnvCreator",
    entry_points = {
        'console_scripts': ['WPDevEnvCreator=WPDevEnvCreator.CommandLine:main'],
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'paramiko'
    ]
)

#Commands to build
#pip install --upgrade setuptools wheel twine
