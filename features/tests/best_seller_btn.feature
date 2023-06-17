# Created by Eugene at 5/31/2023
Feature: Best Seller Links

  Scenario: 5 Links seen
    Given Open Amazon Page
    When Click on Best Sellers
    Then Verify 5 Links
