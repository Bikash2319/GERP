Feature: Test Reset Password functionality of GERP

Scenario: Reset with valid password
    Given User redirect to reset password page
    When User enter valid password in both the fields
    And Click on Reset Password button
    Then Passoword should reset successfully and user redirect to login page

Scenario: Reset with mismatched and invalid password
    Given User redirect to reset password page
    When User enter invalid password in both the fields
    And Click on Reset Password button
    Then Error message should appear to enter valid passwords
    And User enter mismatched password
    Then Password mismatched error message should appear