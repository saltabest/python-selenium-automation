# Created by Eugene at 5/31/2023
Feature: Adding toy to cart
  # Enter feature description here

  Scenario: verify that 1 toys are added
    Given Open Amazon Page
    When Input Toy into search
    And  Click on search
    And Add first product
    And Click add to cart
    And Navigate to cart
    Then Verify cart has right product