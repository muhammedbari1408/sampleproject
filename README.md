# Elevatus
I use chromedriver-binary==111.0.5563.64.0 for the Task. Either Update chrome browser to this version and relaunch the browser or change the version according yours then run requirment file in terminal.
Task is to register candidate and then apply for job.
I used guerilla mail service for signup. In start I navigate to guerrilla mail page to get mail address and then I navigate to elevatus web page. I can perform this with mailinator's API but they are premium.

Important commands:
pip install -r requirements.txt in your terminal
pytest --html=report.html

Getting Started
To get started with this Task, follow these steps:

Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt in your terminal
Download and install the latest version of Google Chrome web browser.
Download and install the corresponding version of ChromeDriver for your Chrome browser.
Open the config.py file and enter your GuerrillaMail email address and password.
Run the tests using pytest in your terminal. use this command in terminal in project dir -> pytest --html=report.html
Task Structure
The task consists of the following files and folders:

chromedriver_binary: a Python module that adds the ChromeDriver binary to the system path.
pages: a folder that contains Python modules representing the different pages of the website.
tests: a folder that contains the Python test modules.
README.md: a Markdown file that contains information about the project.
Pages
The pages folder contains Python modules representing the different pages of the website. Each module contains a PageObject class that represents the page and its elements. The PageObject class contains methods that interact with the page elements and perform actions such as filling out forms and clicking buttons.

The following pages are represented in the pages folder:

GuerrillaMailPage: represents the GuerrillaMail inbox page.
SignupFormPage: represents the signup form page of the website.
EmailInboxPage: represents the email inbox page of the GuerrillaMail website.
ApplyForAJob: represents the job application page of the website.
Tests
The tests folder contains Python test modules that test the website's signup and job application processes using Selenium. Each test module contains one or more test functions that perform specific tests on the website.

The following tests are included in the tests folder:

test_signup: tests the website's signup process by filling out the signup form with random data and verifying that the email address received a verification email.
test_applyForJob: tests the website's job application process by filling out the job application form with random data and verifying that the application was submitted successfully.
Conclusion:
In submit cv page, some fields remain empty because of short time and task was long. Other then that I completed every task.
