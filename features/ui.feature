@ui
Feature: UI Testing

  Scenario: Verify user login through the main page
    Given I open the main page
    When I click "Log in" link in the header
    And I enter valid credentials for an existing user
    And I click "Log in" button
    Then I should be logged in successfully

  Scenario Outline: Search computers by different prices ranges
    Given I open the main page
    When I enter "computer" in the search panel
    And I click "Search" button on the main page
    Then There should be 4 products displayed on the search page
    When I open "Advanced Search"
    When I select "Computers >> Desktops" from the "Category" dropdown
    And I set the "Price range" to From <price_from> to <price_to>
    And I click "Search" button on the search page
    Then There should be <number> products displayed on the search page
    And The first product in the search should have the title "<first_title>"
    Examples:
      | price_from | price_to | number | first_title                   |
      | 800        | 1500     | 3      | Build your own cheap computer |
      | 1000       | 1500     | 1      | Build your own computer       |

  Scenario Outline: Add default computer to cart
    Given I open the main page
    When I navigate to the "Computers" category from the top menu
    And I select the "Desktops" subcategory
    And I open the "<product>" product page
    And I click "Add to cart" button
    Then A success notification bar should be visible in the header
    And The shopping cart should contain 1 products
    Examples:
      | product                       |
      | Build your own cheap computer |
      | Build your own computer       |

  Scenario: Checkout process with logged in user - all default options
    Given I open the main page
    When I click "Log in" link in the header
    And I enter valid credentials for an existing user
    And I click "Log in" button
    When I navigate to the "Books" category from the top menu
    And I open the "Computing and Internet" product page
    And I click "Add to cart" button
    When I open the shopping cart from the link in the header
    And I agree with terms of service by clicking the checkbox
    And I click "Checkout" button
    When I click "Continue" in the Billing Address block
    And I click "Continue" in the Shipping Address block
    And I click "Continue" in the Shipping Method block
    And I click "Continue" in the Payment Method block
    And I click "Continue" in the Payment Information block
    And I click "Confirm" in the Confirm Order block
    Then The completed message should contain the correct text