# Created by wences-sanchez at 22/7/21
Feature: Show the game board to the user
  First step towards getting the full-game experience.
  The features will be incremental.

  Scenario: Show the board of the game
    Given the game has just started
    Then the game board is shown as this example
      """
      - - -
      - - -
      - - -
      """