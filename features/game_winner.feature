# Created by wences-sanchez at 28/7/21

Feature: Decide who is the winner of the game
  Decide which player is the winner at the end, having played the whole game

  Scenario: The 'X' player is the winner

    Given an empty new board
    When the "X" player puts a slot in row "2" and col "2"
    And the "O" player puts a slot in row "1" and col "1"
    And the "X" player puts a slot in row "3" and col "3"
    And the "O" player puts a slot in row "2" and col "1"
    And the "X" player puts a slot in row "3" and col "1"
    And the "O" player puts a slot in row "2" and col "3"
    And the "X" player puts a slot in row "3" and col "2"
    Then the game ends and it outputs "X wins"
