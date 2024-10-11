from setuptools import setup, find_packages

setup(
    name="python-ssg",
    version="0.0.1",
    description="A Python SSG library for dynamically generating static websites",
    keywords='python ssg, static site generation, dynamic static sites',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kayon-ariel/python-ssg",
    project_urls={
        "Homepage": "https://github.com/kayon-ariel/python-ssg",
        "Repository": "https://github.com/kayon-ariel/python-ssg.git",
        "Issues": "https://github.com/kayon-ariel/python-ssg/issues",
    },
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
            'python_ssg=python_ssg.watch:start_rendering',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
