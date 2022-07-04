from behave import *

@when('forgot password: I set my email to "{email}"')
def step_impl(context,email):
    context.forgot_pass.set_email(email)

@When('forgot password: I verify that email validation message is correct')
def step_impl(context):
    context.forgot_pass.verify_email_error_msg()

@When('forgot password: I delete the email')
def step_impl(context):
    context.forgot_pass.delete_email()
@When('forgot password: I set valid email to "{email}"')
def step_impl(context,email):
    context.forgot_pass.set_valid_email(email)

@When('forgot password: I click the send email button')
def step_impl(context):
    context.forgot_pass.click_send_email_button()


@Then('forgot password: I click on Back to Login button')
def step_impl(context):
    context.forgot_pass.click_back_to_login_link()