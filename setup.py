from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SEACodecFake",
    version="1.0.0",
    author="Orchid Chetia Phukan, Girish, Mohd Mujtaba Akhtar, Arun Balaji Buduru",
    author_email="girish281003@gmail.com",
    description="Neural Audio Codec Deepfakes in South-East Asian Languages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Helixometry/SEACodecFake",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
