from behave import *


@When('sign_up: I am new and I want to register')
def step_impl(context):
    context.sign_up_page.navigate_sign_in_page()


@When('sign_up: I click sign up button')
def step_impl(context):
    context.sign_up_page.click_sign_up_button()


@When('sign_up: I click personal button')
def step_impl(context):
    context.sign_up_page.click_personal_button()


@When('sign_up: I click continue button')
def step_impl(context):
    context.sign_up_page.click_continue_button()


@When('sign_up: I send first name "{name}"')
def step_impl(context, name):
    context.sign_up_page.input_first_name(name)


@When('sign_up: I click continue first name button')
def stem_impl(context):
    context.sign_up_page.click_continue_first_name_button()


@When('sign_up: I send last name "{last_name}"')
def step_impl(context, last_name):
    context.sign_up_page.input_last_name(last_name)


@When('sign_up: I click last_name_continue_button')
def step_impl(context):
    context.sign_up_page.click_last_name_continue_button()


@When('sign_up: I set my email to "{email}"')
def step_impl(context, email):
    context.sign_up_page.input_email(email)


@When('sign_up: I receive message:Please enter a valid email address.')
def step_impl(context):
    context.sign_up_page.check_error_message_email()


@When('sign_up: I clear the email field')
def step_impl(context):
    context.sign_up_page.clear_email()


@When('sign_up: The error messages is not displayed anymore!')
def step_impl(context):
    context.sign_up_page.check_error_messages_not_displayed()


@When('sign_up: I can click the continue email button!')
def step_impl(context):
    context.sign_up_page.click_continue_email_button()


@When('sign_up: I send password "{password}"')
def step_impl(context, password):
    context.sign_up_page.input_password(password)


@When('sign_up: I check continue last pass button is displayed!')
def step_impl(context):
    context.sign_up_page.check_continue_button()


@When('sign_up: I clear the password field')
def step_impl(context):
    context.sign_up_page.clear_input_password()


@When('sign_up: I set my password "{password}"')
def step_impl(context, password):
    context.sign_up_page.set_password(password)


@When('sign_up: I click continue last pass button')
def step_impl(context):
    context.sign_up_page.clic_continue_last_pass_button()


@Then('sign_up: I confirm password "{password}"')
def step_impl(context, password):
    context.sign_up_page.confirm_password(password)

@Then('sign_up: I click confirm password')
def step_impl(context):
    context.sign_up_page.click_confirm_password_button()
