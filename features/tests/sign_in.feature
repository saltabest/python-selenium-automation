# Created by Eugene at 5/24/2023
Feature: Test scenarios for Sign In page
  User sees Sign In when clicking on Returns and Orders
  Scenario: User sees Sign in
    Given Open Amazon Page
    When Click Orders
    Then Verify Sign In header is visible
    Then Verify email input field is present
