import time
import random
import os
import string
import pyautogui
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GuerrillaMailPage:
    EMAIL_WIDGET = (By.ID, "email-widget")

    def __init__(self, driver):
        self.driver = driver

    def get_email_address(self):
        # Get unique email address from gurellia domain service.
        email_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_WIDGET))
        return email_element.text


class SignupFormPage:
    DRAWER_HANDLE = (By.XPATH, "//div[@class='drawer-handle']")
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")
    NAME_ERROR_MESSAGE = (By.XPATH, "//div[@class='invalid-feedback d-block error-wrapper']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@name='lastName']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
    CONFIRM_PASSWORD_FIELD = (By.XPATH, "//input[@name='confirmPassword']")
    PHONE_FIELD = (By.XPATH, "//input[@class='form-control inputs']")
    TERMS_CHECKBOX = (By.XPATH, "//label[@class='custom-control-label']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[@class='react-toast-notifications__toast__content css-1ad3zal']")
    WELCOME_TEXT = (By.XPATH, "//h1[@class='Header__Welcome-sc-oh77jp-2 cEEwhG display-2 font-weight-400']")

    def __init__(self, driver):
        self.driver = driver
        self.title = "Career portal"

    def get_title(self):
        return self.driver.title

    def generate_random_first_name(self):
        length = 7
        first_names = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return first_names

    def generate_random_last_name(self):
        length = 7
        last_names = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        return last_names

    def generate_random_password(self):
        # define the character sets to choose from
        uppercase_letters = string.ascii_uppercase
        lowercase_letters = string.ascii_lowercase
        special_characters = '@'
        digits = string.digits

        # combine the character sets and shuffle them
        characters = list(uppercase_letters + lowercase_letters + special_characters + digits)
        random.shuffle(characters)

        # generate the password by selecting random characters
        password = ''
        password += random.choice(uppercase_letters)
        password += ''.join(random.choices(lowercase_letters, k=3))
        password += special_characters
        password += ''.join(random.choices(digits, k=4))

        # shuffle the password characters again
        password = ''.join(random.sample(password, len(password)))


        return password

    def generate_random_phone(self):
        length = 7
        phone = ''.join(random.choices('1234567', k=length))
        phone_number = "312"+phone
        return phone_number


    def open_signup_form(self):
        # open application and click on register button.
        self.driver.execute_script("window.open('https://automations.elevatus.io/', 'new window')")
        self.driver.switch_to.window(self.driver.window_handles[1])
        drawer_handle = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DRAWER_HANDLE))
        drawer_handle.click()

        # click on register button.
        register_link = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.REGISTER_LINK))
        register_link.click()

    def first_name_error(self):
        # get the first name error and assert that.
        first_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        first_name_field.send_keys("u")

        other_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        actions = ActionChains(self.driver)
        actions.move_to_element(other_element).click().perform()

        name_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_ERROR_MESSAGE))
        return name_error_message.text

    def password_error(self):
        # get the first name error and assert that.
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.send_keys("u")

        other_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        actions = ActionChains(self.driver)
        actions.move_to_element(other_element).click().perform()

        password_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_ERROR_MESSAGE))
        return password_error_message.text

    def confirm_password_error(self):
        # get the confirm password error and assert that.
        confirm_password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_FIELD))
        confirm_password_field.send_keys("u")

        other_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        actions = ActionChains(self.driver)
        actions.move_to_element(other_element).click().perform()

        password_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_ERROR_MESSAGE))
        return password_error_message.text

    def last_name_error(self):
        # get the first name error and assert that.
        first_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        first_name_field.send_keys("u")

        other_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.WELCOME_TEXT))
        actions = ActionChains(self.driver)
        actions.move_to_element(other_element).click().perform()

        name_error_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NAME_ERROR_MESSAGE))
        return name_error_message.text


    def fill_signup_form(self, first_name, last_name, email, password, phone):
        # type first name.
        first_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        # type last name.
        last_name_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LAST_NAME_FIELD))
        last_name_field.clear()
        last_name_field.send_keys(last_name)

        # type email address we got from guerilla email service.
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        email_field.send_keys(email)

        # type password.
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        password_field.send_keys(password)

        # type confirm password value.
        confirm_password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CONFIRM_PASSWORD_FIELD))
        confirm_password_field.send_keys(password)
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
        time.sleep(2)

        # type phone number.
        phone_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.PHONE_FIELD))
        phone_field.send_keys(phone)

        # check term checkbox.
        terms_checkbox = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.TERMS_CHECKBOX))
        terms_checkbox.click()
        submit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUBMIT_BUTTON))
        submit_button.click()
        time.sleep(3)

        success_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))

        # return the text of the success message
        return success_message.text

class EmailInboxPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_email_list(self):
        # Wait for the email list to appear
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email_list")))

    def click_verification_email(self):
        # Click on the verification email.
        verification_email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tbody[@id='email_list']//td[contains(text(),'info@elevatus.io')]")))
        verification_email.click()

    def click_verification_link(self):
        # Click on the verification link in the email.
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
        verification_link = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Click Here')]")))
        verification_link.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

class ApplyForAJob:

    DRAWER_HANDLE = (By.XPATH, "//div[@class='drawer-handle']")
    FILL_MANUALLY = (By.XPATH, "//button[contains(text(),'Fill in manually')]")
    JOBS = (By.XPATH, "//div[contains(text(),'Jobs')]")
    JOB_TITLE = (By.XPATH, "//input[@name='query']")
    CAREER_LEVEL = (By.XPATH, "//input[@id='careerLevel']")
    CAREER_LEVEL_VALUE = (By.XPATH, "//li[@id='careerLevel-option-1']")
    SKILL_FIELD = (By.XPATH, "//div[@class=' css-1hwfws3']")
    SKILL_FIELD_VALUE = (By.XPATH, "//div[@id='react-select-2-option-0']")
    SEARCH_BUTTON = (By.XPATH, "//button[@class= 'btn-main text-white w-100 mx-1 btn btn-outline-secondary']")
    VIEW_RESULTS = (By.XPATH, "//span[contains(text(), 'View')]")
    APPLY_FOR_JOB = (By.XPATH, "//span[contains(text(), 'Apply')]")
    DESCRIPTION_FIELD = (By.XPATH, "//textarea[@id='description']")
    BUILD_PROFILE_PAGE = (By.XPATH, "//h1[@class='Header__Welcome-sc-oh77jp-2 cEEwhG display-2 font-weight-400']")

    # job submit form
    SUBMIT_CV_MESSAGE = (By.XPATH, "//strong[text()='Submit Your CV']")
    DATE_PICKER = (By.XPATH, "//input[@id='date-picker-dialog']")
    GENDER_BUTTON = (By.XPATH, "//input[@id='gender']")
    GENDER_BUTTON_VALUE = (By.XPATH, "//li[@id='gender-option-0']")
    NATIONALITY_BUTTON = (By.XPATH, "//input[@id='nationality']")
    NATIONALITY_BUTTON_VALUE = (By.XPATH, "//li[@id='nationality-option-0']")
    ADDRESS_FIELD = (By.XPATH, "//input[@id='address']")
    CITY_FIELD = (By.XPATH, "//input[@id='city']")
    COUNTRY_DROPDOWN = (By.XPATH, "//input[@id='location.country_uuid']")
    COUNTRY_DROPDOWN_VALUE = (By.XPATH, "//li[@id='location.country_uuid-option-2']")
    JOB_TYPE_DROPDOWN = (By.XPATH, "//input[@id='job_types']")
    JOB_TYPE_VALUE = (By.XPATH, "//li[@id='job_types-option-0']")
    CV_UPLOAD = (By.XPATH, "//div[@class='col-lg-12']//div//div[@role='button']")
    WILLING_TO_TRAVEL_VALUE = (By.XPATH, "//li[@id='SharedAutocompleteControl--0---0-0-willing_to_travel-option-0']")
    SKILLS_SET = (By.XPATH, "//input[@placeholder='Type your skill here and click on enter to add another skill.']")
    SUBMIT_AND_APPLY_BUTTON =(By.XPATH, "//span[text()='Submit profile and apply']")
    APPLIED_BUTTON = (By.XPATH, "//button[@class='btn-main ml-sm-auto cursor-not-allowed btn btn-secondary disabled']")

    def __init__(self, driver):
        self.driver = driver


    def buid_profile(self):
        drawer_handle = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DRAWER_HANDLE))
        drawer_handle.click()
        time.sleep(5)
        build_profile_page = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.BUILD_PROFILE_PAGE))
        return build_profile_page.text
    def click_fill_in_manually(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        self.driver.execute_script("window.scrollBy(0, window.innerHeight/2);")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.FILL_MANUALLY))
        fill_manually = self.driver.find_element(*self.FILL_MANUALLY)
        fill_manually.click()

    def click_jobs_button(self):
        # click on job button on dashboard.
        jobs = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOBS))
        jobs.click()


    def fill_search_form(self, job_title):
        # fill job title field.
        job_title_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_TITLE))
        job_title_field.send_keys(job_title)

        # select career level from dropdown.
        career_level_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CAREER_LEVEL))
        career_level_field.click()
        career_level_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CAREER_LEVEL_VALUE))
        career_level_value.click()

        # click on search button.
        search_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SEARCH_BUTTON))
        search_button.click()

    def open_search_results(self):
        # click on view button from job description.
        view_reults = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.VIEW_RESULTS))
        view_reults.click()
        time.sleep(5)

    def click_apply_button(self):
        self.driver.execute_script("window.scrollTo(0, 1000)")
        time.sleep(3)

        # click on apply button.
        apply_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.APPLY_FOR_JOB))
        apply_button.click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))


    def submit_cv_page(self):
        submit_cv_message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUBMIT_CV_MESSAGE))
        return submit_cv_message.text

    def submit_profile_and_apply(self):
        # fill description field in submit form
        description_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DESCRIPTION_FIELD))
        description_field.send_keys("This is for testing")

        # Select a random date and select it from date picker
        year = str(random.randint(1990, 2000))
        month = str(random.randint(1, 12)).zfill(2)
        day = str(random.randint(1, 28)).zfill(2)
        date = f"{year}-{month}-{day}"

        date_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.DATE_PICKER))
        date_button.send_keys(date)

        # select gender from dropdown
        gender_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.GENDER_BUTTON))
        gender_button.click()
        gender_button_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.GENDER_BUTTON_VALUE))
        gender_button_value.click()

        # select nationality from dropdown
        nationality_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NATIONALITY_BUTTON))
        nationality_button.click()
        nationality_button_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.NATIONALITY_BUTTON_VALUE))
        nationality_button_value.click()

        # Type address
        address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ADDRESS_FIELD))
        address_field.send_keys("This is testing")
        self.driver.execute_script("window.scrollTo(0, 250)")
        time.sleep(2)

        # type city
        city_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CITY_FIELD))
        city_field.send_keys("This is testing")

        # select country from dropdown
        country_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COUNTRY_DROPDOWN))
        country_dropdown.click()
        country_dropdown_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.COUNTRY_DROPDOWN_VALUE))
        country_dropdown_value.click()
        time.sleep(2)

        # select job type from dropdown
        self.driver.execute_script("window.scrollTo(570, 688)")
        time.sleep(3)
        job_type_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_TYPE_DROPDOWN))
        job_type_dropdown.click()
        job_type_dropdown_value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.JOB_TYPE_VALUE))
        job_type_dropdown_value.click()

        # Upload cv which is in document folder.
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'documents', "Umer's Resume (2).pdf")
        cv_upload = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CV_UPLOAD))
        cv_upload.click()
        pyautogui.sleep(1)
        pyautogui.typewrite(file_path)
        pyautogui.press("enter")
        time.sleep(5)

        # Type skill set
        skill_set = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SKILLS_SET))
        skill_set.send_keys("Automation")
        skill_set.send_keys(Keys.ENTER)
        skill_set.send_keys("QA")
        skill_set.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

        # click on submit button to submit application.
        submit_apply_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUBMIT_AND_APPLY_BUTTON))
        submit_apply_button.click()
        time.sleep(2)


    def assert_button_is_disabled(self):
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        applied_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.APPLIED_BUTTON))
        assert not applied_button.is_enabled(), 'The button should be disabled.'




