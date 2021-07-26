# Created by wences-sanchez at 22/7/21
Feature: Show the game board to the user
  First step towards getting the full-game experience.
  The features will be incremental.

  Scenario Outline: Show the board of the game
    Given the game is started
    When the user inputs <input>
    Then the game board is shown like <output>

    Examples: Game boards
      | input     | output |
      | O_OXXO_XX | ---------\n\| O _ O \|\n\| X X O \|\n\| _ X X \|\n---------\n |
      | OXO__X_OX | ---------\n\| O X O \|\n\| _ _ X \|\n\| _ O X \|\n---------\n |
      | _XO__X___ | ---------\n\| _ X O \|\n\| _ _ X \|\n\| _ _ _ \|\n---------\n |
