Feature:  Test the project onboarding process of GenSOM ERP

@login_required
Scenario: Onboard a project in valid way
Given User should redirect to Make master and enter a make
And User should redirect to Category master and enter a category
And User should redirect to Model master and enter a model
And User should redirect to sub category master and enter a sub-category
And User should redirect to warehouse master and enter a warehouse
And User should redirect to inventory master and enter an inventory
And User should redirect to project management and fill out basic details page
And User navigate to site person tab and enter a User
And User navigate to logger tab and enter a logger
And User navigate to the equipment tab and enter equipment name to enter all the equipments
Then User navigate to the project management page and make the project live
Then Added project successfully displayed on the overview dashboard page

