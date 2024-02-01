# Практикум SDET: тестовое задание
Registration test with registartion form page based on 
https://demoqa.com/automation-practice-form

# Installation
1. Get it from GIT repository: ``git clone git@github.com:denzel-commits/sdet-practicum-test-task.git``
2. Go to project folder: ``cd sdet-practicum-test-task``
3. Create virtual environment: ``python3 -m venv venv``
4. Activate virtual environment: ``source venv/bin/activate``
5. Install dependencies: ``python -m pip install -r requirements.txt``

This installs all required modules.

# Running the Tests
To run tests with default settings defined in "pytest.ini" execute the following command:

``python -m pytest``

# Generate reports
By default "allure-results" folder will be created with test results.
In order to generate report from it run the following command:

``allure generate .\allure-results --clean``

# Options
* --base_url: required option - specify target page URL
* --browser: is optional, browser name (chrome | firefox), default=chrome
* --logging_level: is optional, log level (INFO | WARNING | ERROR), default=WARNING
* --headless: is optional, to run browser in headless mode
* --tolerance: is optional, timeout in seconds, default=5 
 
# Usage examples
``python3 -m pytest --base_url=https://demoqa.com/automation-practice-form --headless``

``python3 -m pytest --base_url=https://demoqa.com/automation-practice-form --browser=firefox --logging_level=WARNING``

``python3 -m pytest --base_url=https://demoqa.com/automation-practice-form --headless --tolerance=3``