from behave import given, then

from src.core.TicTacToe import TicTacToe


@given('the game has just started')
def step_impl(context):
    context.game = TicTacToe()


@then('the game board is shown as this example')
def step_impl(context):
    assert context.game.__eq__(context.text)
