# Created by wences-sanchez at 22/7/21
Feature: Show the table to the user
  First step towards getting the full-game experience.
  The features will be incremental.

  Scenario: Show the table of the game
    Given the game has just started
    When a user begins the game
    Then the game table is shown