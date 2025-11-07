from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='medkit',
    version='1.0.0',
    description='Medical Information and Reference System',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='MedKit Contributors',
    url='https://github.com/csverma610/medkit',
    project_urls={
        'Bug Tracker': 'https://github.com/csverma610/medkit/issues',
        'Documentation': 'https://medkit.readthedocs.io',
        'Source Code': 'https://github.com/csverma610/medkit',
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'google-genai>=0.3.0',
        'pydantic>=2.0.0',
        'requests>=2.28.0',
        'networkx>=3.0',
        'matplotlib>=3.6.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
            'pytest-xdist>=3.0',
            'black>=22.0',
            'flake8>=5.0',
            'mypy>=0.990',
            'isort>=5.11.0',
        ],
        'docs': [
            'sphinx>=5.0',
            'sphinx-rtd-theme>=1.0',
            'sphinx-autodoc-typehints>=1.18.0',
        ],
    },
    python_requires='>=3.8',
    entry_points={
        'console_scripts': [
            'medkit=medkit.__main__:main',
        ],
    },
    keywords=['medical', 'healthcare', 'ai', 'gemini', 'diagnosis', 'drug-interactions'],
    license='MIT',
)
