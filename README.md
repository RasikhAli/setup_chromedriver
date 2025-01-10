# setup_chromedriver

`setup_chromedriver` is a Python library to automatically manage and set up ChromeDriver for Selenium projects. It ensures compatibility between your Chrome browser and ChromeDriver versions.

---

## About the Creator

This library was created by **[Rasikh Ali](https://www.linkedin.com/in/rasikh-ali/)**. Rasikh is a passionate developer dedicated to creating tools that simplify development workflows and improve efficiency.

- **GitHub**: [github.com/RasikhAli](https://github.com/RasikhAli)
- **LinkedIn**: [linkedin.com/in/rasikh-ali](https://www.linkedin.com/in/rasikh-ali/)
- **Marvelous Software Solutions**: [linkedin.com/company/marvelous-software-solutions/](https://www.linkedin.com/company/marvelous-software-solutions/)

Feel free to connect or explore more of his projects!

---

## Installation

```bash
pip install setup_chromedriver
```

## Usage

```python
from setup_chromedriver import setup_chrome_driver

driver = setup_chrome_driver()
driver.get("https://example.com")
```

## Features

- Automatically detects your Chrome version.
- Downloads and sets up the compatible ChromeDriver version.
- Easy integration with Selenium scripts.

## License

This project is licensed under the MIT License.