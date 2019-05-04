from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="Cyber-RSA",
    version="1.0.0",
    description="Cipher-RSA",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/IamSantoshKumar/Python",
    author="Santhoshkumar",
    author_email="shanvsanthosh@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["CyberRSA"],
    include_package_data=True,
    install_requires=["Crypto"],
    entry_points={
        "console_scripts": [
            "Cyber-RSA=CyberRSA.Cipher:main",
        ]
    },
)