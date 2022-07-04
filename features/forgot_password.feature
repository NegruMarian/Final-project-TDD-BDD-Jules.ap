Feature: Jules.app forgot password test
  Background:                 # defineste faptul ca acel ghiven/when o sa fie valabil pentru toate scenariile
    Given sign in: I am a user on jules sign in page
                              # contextul in care se efectueaza testarea

    @jules1
    Scenario: Wrong email message validation
                              # am trecut ce vrem sa testam
      When sign in: I click the forgot password link
      When forgot password: I set my email to "abc"
      When forgot password: I verify that email validation message is correct
      When forgot password: I delete the email
      When forgot password: I set valid email to "abc@gmail.com"
      When forgot password: I click the send email button
      Then forgot password: I click on Back to Login button


    @jules2
    Scenario Outline: wrong email validation message with table data
    When sign in: I click the forgot password link
    When forgot password: I set my email to "<email_address>"
    When forgot password: I verify that email validation message is correct
    Then forgot password: I click on Back to Login button

    Examples:
      | email_address |
      | abcde.com     |
      | abc           |

  Scenario Outline: Forgot pass cu tabel de valori
    When login: user clicks on forgot pass button
    When forgot_pass: user enters email address in email input "<valid_email>"
    Then forgot_pass: verify that send email button is enabled

    Examples:
      | valid_email             |
      | itfactory1.ro@gmail.com |
      | itfactory2.ro@gmail.com |
      | itfactory3.ro@gmail.com |


  Scenario: Click on back to login
    When forgot password: I click on Back to Login button
    Then sign in page: I am returned to the homepage