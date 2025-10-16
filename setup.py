from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="heic-to-jpg",
    version="1.0.0",
    author="OT",
    author_email="olof.thornell@gmail.com",
    description="A command line tool to convert HEIC files to JPG format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/user-olof/ConvertHeicToJpg",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "Pillow>=8.0.0",
        "pillow-heif>=0.10.0",
    ],
    entry_points={
        "console_scripts": [
            "heic-to-jpg=convert_to_jpg:main",
        ],
    },
    keywords="heic jpg jpeg convert image",
    project_urls={
        "Bug Reports": "https://github.com/user-olof/ConvertHeicToJpg/issues",
        "Source": "https://github.com/user-olof/ConvertHeicToJpg",
    },
)