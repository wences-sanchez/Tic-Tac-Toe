from src.core.TicTacToe import TicTacToe

from behave import *


@given("the game is started")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given the game is started')


@when("the user inputs {user_input}")
def step_impl(context, user_input):
    """
    :type context: behave.runner.Context
    :type user_input: str
    """
    raise NotImplementedError(u'STEP: When the user inputs <input>')


@then("the game board is shown like {user_output}")
def step_impl(context, user_output):
    """
    :type context: behave.runner.Context
    :type user_output: str
    """
    raise NotImplementedError(
        u'STEP: Then the game board is shown like <output>')