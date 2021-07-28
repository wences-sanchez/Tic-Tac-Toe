# Created by wences-sanchez at 22/7/21

# NOTE: This .feature file has been duplicated because the strings
# of the game boards didn't fit in one line and didn't recognize
# properly the '\n' characters.

Feature: Show the game board to the user
  First step towards getting the full-game experience.
  The features will be incremental.

  Scenario: Show the 1st board of the game

    Given the game is started
    When the user inputs "O_OXXO_XX"
    Then the game board is shown like this
      """
      ---------
      | O _ O |
      | X X O |
      | _ X X |
      ---------
      """

  Scenario: Show the 2nd board of the game

    Given the game is started
    When the user inputs "OXO__X_OX"
    Then the game board is shown like this
      """
      ---------
      | O X O |
      | _ _ X |
      | _ O X |
      ---------
      """

  Scenario: Show the 3rd board of the game

    Given the game is started
    When the user inputs "_XO__X___"
    Then the game board is shown like this
      """
      ---------
      | _ X O |
      | _ _ X |
      | _ _ _ |
      ---------
      """

