
import chromedriver_binary  # Adds chromedriver binary to path
import pytest
from selenium import webdriver
from pages import GuerrillaMailPage, SignupFormPage, EmailInboxPage, ApplyForAJob

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_signup(driver):
    guerrilla_mail_page = GuerrillaMailPage(driver)
    signup_form_page = SignupFormPage(driver)
    email_inbox_page = EmailInboxPage(driver)


    # On every signup we need unique email address. Get email address here and goes to signup form page.
    driver.get("https://www.guerrillamail.com/")
    driver.maximize_window()
    email_address = guerrilla_mail_page.get_email_address()

    # Open the signup form
    signup_form_page.open_signup_form()

    # assert title of page.
    assert signup_form_page.get_title() == signup_form_page.title, "Title does not match."

    # Assert first name error message.
    first_name_error_message = signup_form_page.first_name_error()
    assert first_name_error_message == "First name must be at least 3 characters"

    last_name_error_message = signup_form_page.last_name_error()
    assert last_name_error_message == "Last name must be at least 3 characters"

    # password errors assertions
    password_error_message = signup_form_page.password_error()
    assert password_error_message == "Password must be at least 8 characters"

    confirm_password_error_message = signup_form_page.confirm_password_error()
    assert confirm_password_error_message == "Password must be at least 8 characters"

    # genrate random data and fill form with that.
    random_first_name = signup_form_page.generate_random_first_name()
    random_last_name = signup_form_page.generate_random_last_name()
    random_password = signup_form_page.generate_random_password()
    random_phone = signup_form_page.generate_random_phone()
    # Fill out the signup form
    success_message = signup_form_page.fill_signup_form(random_first_name, random_last_name, email_address, random_password, random_phone)

    assert success_message == "Email Sent Successfully! Follow the instructions sent to your email to complete your registration."
    driver.close()

    # Verify email address received the verification email
    driver.switch_to.window(driver.window_handles[0])
    driver.get("https://www.guerrillamail.com/inbox")

    # assert that we are on right page.
    assert "https://www.guerrillamail.com/inbox" in driver.current_url
    driver.refresh()
    email_inbox_page.wait_for_email_list()



    # open email we received for verification.
    email_inbox_page.click_verification_email()

    # click on verification link.
    email_inbox_page.click_verification_link()
    driver.switch_to.window(driver.window_handles[1])

def test_applyForJob(driver):
    apply_for_job = ApplyForAJob(driver)


    # assert that we are on right page.
    build_page_message = apply_for_job.buid_profile()
    assert build_page_message == "Building your profile"

    # click on fill page manually.
    apply_for_job.click_fill_in_manually()

    # Click on job button on dashboad
    apply_for_job.click_jobs_button()

    # fill searchbar to find relative job.
    apply_for_job.fill_search_form("QA")

    # open job link which we get from search result.
    apply_for_job.open_search_results()

    # Click on apply button from job description.
    apply_for_job.click_apply_button()

    # assert that we are on submit cv page.
    submit_cv_message = apply_for_job.submit_cv_page()
    assert submit_cv_message == "Submit Your CV"


    # Fill form and submit the application.
    apply_for_job.submit_profile_and_apply()

    # assert applied button is not enabled.
    apply_for_job.assert_button_is_disabled()



