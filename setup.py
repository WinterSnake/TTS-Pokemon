from setuptools import setup, find_packages

setup(
    name="tts-pokemon",
    version="1.0.0",
    author="Ryan Smith",
    author_email="smith.a.ryan.98@gmail.com",
    description="A Pokemon deck generator for Tabletop Simulator",
    license="MIT",
    url="https://github.com/WinterSnake/TTS-Pokemon",
    python_requires=">=3.10",
    install_requires=['aiohttp', 'bs4'],
    packages=find_packages(include=['tts-pokemon', 'tts-pokemon.*']),
)
