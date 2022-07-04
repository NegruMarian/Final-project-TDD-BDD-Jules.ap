Feature: Jules.app sign_in test
  Background:                 # defineste faptul ca acel ghiven/when o sa fie valabil pentru toate scenariile
    Given sign in: I am a user on jules sign in page
                              # contextul in care se efectueaza testarea

    @jules
    Scenario: Input correct email
                              # am trecut ce vrem sa testam

      When sign in: I set my email to "{aaaaa@gmail.com}"
      When sign in: I set my password to "p"
      When sign_in: I delete password
      When sign in : I check the login button is disabled
      Then sign in: I verify error- Please enter your password!
