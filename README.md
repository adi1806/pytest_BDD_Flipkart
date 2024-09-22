# Python BDD Framework with pytest

## Project Description

This project is a Behavior-Driven Development (BDD) test automation framework using pytest and pytest-bdd. The framework is designed to validate various functionalities of a Flipkart web application using Selenium WebDriver.

## Table of Contents

- Project Description
- Setup Instructions
- Usage
- Test Cases
- Keywords
- Resources
- Contributing
- License

## Setup Instructions

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Google Chrome (or any other browser you want to use)
- ChromeDriver (or the corresponding driver for your browser)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Ensure the ChromeDriver (or the corresponding driver for your browser) is in your PATH.

## Usage

### Running Tests

To run the tests and generate an Allure report, use the following command:

```bash
pytest --alluredir=allure-results
