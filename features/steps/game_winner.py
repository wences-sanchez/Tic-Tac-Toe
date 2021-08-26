from src.core.TicTacToe import TicTacToe

from behave import given, then, step


@given('an empty new board')
def an_empty_new_board(context):
    context.tic_tac_toe = TicTacToe('')


@step('the "{player}" player puts a slot in row "{row}" and col "{col}"')
def put_a_slot_in_board(context, player, row, col):
    context.tic_tac_toe.set_value_in_cell(int(row), int(col), player)


@then('the game ends and it outputs "{final_msg}"')
def the_game_ends_and_it_outputs_msg(context, final_msg):
    assert context.tic_tac_toe.get_status() == final_msg
