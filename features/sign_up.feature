Feature: Jules.app sign_up test
  Background:                 # defineste faptul ca acel ghiven/when o sa fie valabil pentru toate scenariile
    Given sign in: I am a user on jules sign in page
                              # contextul in care se efectueaza testarea

    @juless
    Scenario: I creat an personal account
                              # am trecut ce vrem sa testam

      When sign_up: I click sign up button
      When sign_up: I click personal button
      When sign_up: I click continue button
      When sign_up: I send first name "marian"
      When sign_up: I click continue first name button
      When sign_up: I send last name "negru"
      When sign_up: I click last_name_continue_button
      When sign_up: I set my email to "asad"
      When sign_up: I receive message:Please enter a valid email address.
      When sign_up: I clear the email field
      When sign_up: I set my email to "@yahoo.com"
      When sign_up: The error messages is not displayed anymore!
      When sign_up: I can click the continue email button!
      When sign_up: I send password "asdfg"
      When sign_up: I check continue last pass button is displayed!
      When sign_up: I clear the password field
      When sign_up: I set my password "Asdfgh1#"
      When sign_up: I click continue last pass button
      Then sign_up: I confirm password "asdfgAsdfgh1#"
      Then sign_up: I click confirm password