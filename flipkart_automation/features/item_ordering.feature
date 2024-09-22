Feature: Item ordering on Flipkart

 Scenario: Order items and verify cart
    Given I open Flipkart
    When I search for "Samsung S22 128 GB" and select the second item
    And I check the item's availability and add it to the cart
    And I return to the home page
    And I search for "bajaj iron majesty" and select the second item
    And I check the item's availability and add it to the cart
    Then I navigate to the cart
    And I verify both items are present in the cart
    And I verify the total price reflects the sum of both items
    When I remove one item from the cart
    Then I confirm the total price is updated accordingly