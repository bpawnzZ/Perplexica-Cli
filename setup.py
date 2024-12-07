from setuptools import setup, find_packages

setup(
    name="perplexica-cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
    ],
    entry_points={
        'console_scripts': [
            'perplexica-search=perplexica_cli.perplexica_search:main',
            'perplexica-simple=perplexica_cli.perplexica_simple:main',
        ],
    },
    python_requires='>=3.7',
    author="Perplexica Team",
    description="CLI tools for Perplexica Search API",
    long_description="Command line interfaces for interacting with the Perplexica Search API",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
