Feature: Test login functionality of GERP

Scenario: Login using valid credentials
    Given User should navigate to login page
    When User enter valid email and Password
    And User click on Login button
    Then User should able to logged into the application and Overview Dashboard page should be displayed

Scenario: Login using invalid credentials
    Given User should navigate to login page
    When User enter invalid email and invalid Password
    And User click on Login button
    Then User should not able to logged in and error toaster message should displayed