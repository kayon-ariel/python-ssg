from setuptools import setup, find_packages

setup(
    name="python-ssr",
    version="0.0.4",
    description="A Python SSR library for dynamically rendering static websites",
    keywords='python ssr, ssr, server side rendering, server-side-rendering',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kayon-ariel/Python-SSR",
    project_urls={
        "Homepage": "https://github.com/kayon-ariel/Python-SSR",
        "Repository": "https://github.com/kayon-ariel/Python-SSR.git",
        "Issues": "https://github.com/kayon-ariel/Python-SSR/issues",
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
