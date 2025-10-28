Feature: Test all the functionality of Make module

@login_required
Scenario: Test the make module is interactable
Given User logged into the application
When User click on Make sub-menu from Master menu
Then User successfully redirect to make master page

@login_required
Scenario: Verify by adding a valid make
Given User logged into the application
When User click on Make sub-menu from Master menu
And User click on add make button
Then User enters the make and click on save button
Then Make is successfully saved into the system
