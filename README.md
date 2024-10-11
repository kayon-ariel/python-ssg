## Python-SSG: Static Site Generation with Python

A library for generating HTML pages on the server, allowing dynamic content updates from APIs while serving static files.

![Python Version](https://img.shields.io/badge/python-%3E%3D3.6-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

[![PyPI Latest Release](https://img.shields.io/pypi/v/python-ssg.svg)](https://pypi.org/project/python-ssg/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/python-ssg.svg?label=PyPI%20downloads)](https://pypi.org/project/python-ssg/)

## Table of Contents

- [What is SSG](#what-is-ssg)
- [Use Cases](#use-cases)
- [Installation](#installation)
- [Usage](#usage)
- [Example Structure for Usage](#example-structure-for-usage)
- [Example of HTML](#example-of-indexhtml)
- [Contribution](#contribution)
- [Running Tests](#running-tests)

## What is SSG

**Static Site Generation (SSG)** is a technique where HTML pages are generated on the server and served as static files. This allows for better initial performance and improved SEO optimization, as search engines can easily index the content. With SSG, applications provide a faster and smoother user experience, especially on mobile devices, making content delivery more efficient and accessible. The key advantage of SSG is that the pages can be dynamically updated with data from APIs while remaining static in nature.

### Use Cases

Python-SSG is ideal for those who need to generate static pages that dynamically update with data from APIs. Here are some use cases:

- **Personal Blogs**: Dynamically update the main and post pages with the latest content at defined intervals.
- **Report Pages**: Generate pages with report data that automatically update, using APIs that provide statistics or charts.
- **Dynamic Landing Pages**: Create landing pages that update as the API receives new data, such as promotions or product updates.

## Installation

To install the library, you can use the following command:

```bash
pip install python-ssg
```

## Usage

1. **Create a configuration file (`config.json`)**:

   The file should contain the following structure:

   ```json
   {
     "pages": {
         "index": {
             "api": {
                 "url": "http://127.0.0.1:5000/api/index",
                 "method": "GET"
             },
             "render_interval": 5
         }
     }
   }
   ```

Each page corresponds to an HTML template file in the `/html/` directory, and the result is rendered in the `/dist/` directory. The defined API returns JSON, which is used to populate the template. This JSON can come from local APIs, as in the example, or any external API you wish to use.

2. **Start Rendering**:

   To start rendering, you should call the `start_rendering` function and pass the path of your configuration file.

   ```python
   from python_ssg import start_rendering

   if __name__ == "__main__":
       start_rendering("config.json")
   ```

## Example Structure for Usage

Here is an example directory structure for using the library:

```
your_project/
  - config.json
  - html/
    - assets/
      - (Your folders and files)
    - index.html
    - (Your HTML files)
  - dist/
    - (rendered HTML files)
  - main.py
```

### Example of `index.html`

An example HTML file that uses variables for rendering:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/style.css">
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <p>{{ description }}</p>
    <script src="assets/script.js"></script>
</body>
</html>
```

## Contribution

Feel free to explore, open issues, suggest pull requests, or just enjoy learning from the code!

### Future Implementations: Integration with AWS S3

A planned future improvement for the project is the possibility of integrating Python-SSG with AWS S3. This will allow the generated static pages to be automatically uploaded to a bucket on S3, keeping the site online and always updated with the latest content without the need to manage servers.

It’s not implemented yet, but it would be extremely useful for those looking to automate the update of static pages hosted in the cloud, keeping everything synchronized with real-time APIs.

## Running Tests

To ensure that all library features are working correctly, it is important to run tests. You can do this using Python's `unittest` module.

Follow the steps below to run the tests:

1. Navigate to the root directory of your project.

2. Execute the following command:

   ```bash
   python -m unittest discover -s tests -p "*.py"
   ```
