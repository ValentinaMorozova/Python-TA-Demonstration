# UI and API Test Automation Demonstration

## Purpose
This project serves as a demonstration of my skills in test automation for a QA technical assignment. It includes two types of automated tests: **UI tests**  and **API tests**.

The original task can be found in the file **docs/Task.docx**

## Systems Under Test
- UI tests check the behavior of https://demowebshop.tricentis.com, a demo web shop with a mock payment interface.

- API tests check the REST-API for https://openlibrary.org/; documentation is available [here](https://openlibrary.org/developers/api).

## Solution
This project is developed in Python and utilizes several key libraries to implement the test automation solution. For test declaration, I used the `behave` BDD framework, `selenium` is employed for UI testing and `requests` is used for API testing. To ensure clean and maintainable code, I applied the **Page Object Pattern** for organizing UI test elements and actions.

Test reports are generated in a simple HTML format using the `behave-html-formatter` library.

### Requirements
To get started, you need to have `Python 3.12.7` or later. To install all dependencies, you can use `pip` package installer.
Requirements are listed in the `requirements.txt` file, so you can simply run:

> pip install -r requirements.txt

### Environment
The solution was created and tests on Windows 11. For other systems, some adjustments might be needed.

UI tests require `Google Chrome` browser. It must be installed on your machine to run the tests.

### Run tests
Tests could be run via the command line in main directory.

To run all tests from both features with default options, save reports in HTML format in the **reports/report.html** file and keep logs in **logs/test_log.log** file, run this command:
> behave -f html -o reports/report.html --no-logcapture

To run a specific feature, add its filename to `behave` command. For example:
> behave features/api.feature -f html -o reports/api_report.html --no-logcapture

### Internal structure
- **api_models**: Contains the Python code for API models. Currently, it includes only one file, but can be extended as needed for future API endpoints.
- **docs**: Stores all documentation related to the project. This includes:
  - **B-UI-001.png** – screenshot for bug report;
  - **Task.docx** – task description;
  - **Test cases.xlsx** – traceability matrix;
  - **Test results.xlsx** – bug report.
- **features**: Contains the high-level code for the automated tests. This includes:
  - **steps** - subdirectory holds Python code for implementing test steps;
  - **api.feature** - defines the API tests, written in the _Gherkin_ syntax;
  - **environment.py** - defines the setup and teardown methods, configures logging and browser, and contains common variables.
  - **ui.feature** - defines the UI tests, written in the _Gherkin_ syntax;
- **logs**: Stores example log files generated during test execution.
- **pages**: Implements the **Page Object Pattern** by containing page classes that organize UI elements and actions for the tests.
- **reports**: Contains HTML reports generated from the test results.