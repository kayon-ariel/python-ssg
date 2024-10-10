from setuptools import setup, find_packages

setup(
    name="python-ssr",
    version="0.0.1",
    description="A Python SSR library for dynamically rendering static websites",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kayon-ariel/Python-SSR",
    author="Kayon Ariel",
    author_email="kayonariel@gmail.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'jinja2',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'python_ssr=python_ssr.watch:start_rendering',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
