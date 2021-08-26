from behave import *

from src.core.TicTacToe import TicTacToe


@given('the game is started')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when('the user inputs "{user_input}"')
def step_impl(context, user_input):
    """
    :type context: behave.runner.Context
    :type user_input: str
    """
    context.response = TicTacToe(user_input)


@then('the game board is shown like this')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    assert str(context.response) == context.text
