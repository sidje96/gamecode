# The standard python installation includes the unittest framework, which is enough for most normal test cases.
# Unit tests can be autodiscovered and ran by executing a command like `python -m unittest` from the project root folder.
# For more information see the docs https://docs.python.org/3/library/unittest.html
import unittest
from unittest import mock

# I renamed the code file as python imports don't play nice with dashes and files starting with numbers.
# There are other ways to get around this, but it's good practice to keep this in mind when naming files.
# The __init__.py file is also necessary for python to easily discover the local project file you want to import.
import game_100_game


class Test100Game(unittest.TestCase):
    """
    Keeping tests in a class can be very useful for organization.
    Especially when you need setUp and tearDown functions that apply to each individual test.
    """

    # Every function starting with test will be recognized as an individual test by the unittest framework.
    def test_given_default_globals_when_check_win_should_return_false(self):
        """
        As with normal function and variables, naming is also very important when writing tests.
        I like to use the format "given" any assumption/defaults, "when" action, "should" have a certain result,
        to have a very descriptive test name that makes it easy to check what a test should be doing.
        """
        # An assertion (there is lots of different types) will fail the program if it doesn't match the condition
        self.assertFalse(game_100_game.check_win())

    def test_given_current_score_more_than_100_when_check_win_should_return_true(self):
        """
        Global variables (compared to class properties and function arguments) can make testing a little harder.
        Python does allow overwriting them, but that overwrite is not limited to the scope of this specific test.
        So it will mess with other tests, since unittest executes all of them in parallel.
        Individually this test and its counterpart succeed, but when executed simultaneously the other one will fail.
        """
        game_100_game.CURRENT_SCORE = 105
        self.assertTrue(game_100_game.check_win())

    def test_given_human_player_and_input_when_plays_should_increase_score(self):
        """
        Mocking and patching can be very useful for functions that are out of your control (like input),
            that depend on external factors (like one that would send and email),
            or that you don't want to test at that moment.
        Mock frameworks (like unittest) have the capability to intercept and capture object and function calls.
        This allows you to set the results of those calls in your tests without the function being executed.
        """
        game_100_game.PLAYER_AMOUNT = 2
        game_100_game.CURRENT_PLAYER = "Player 1"
        game_100_game.CURRENT_SCORE = 50
        with mock.patch("game_100_game.input") as mock_input:
            mock_input.return_value = "5"
            game_100_game.player()

        self.assertEqual(55, game_100_game.CURRENT_SCORE)

    @mock.patch("game_100_game.random")
    @mock.patch("game_100_game.input")
    def test_given_incorrect_input_when_plays_should_raise_TypeError(self, mock_input, mock_random):
        """
        Most context handlers (with ... as .. statements) can also have a decorator (@) form doing the same thing.
        For mocking/patching that can be easier to read, especially if you need to mock more than 1 thing.
        Although the order of function arguments can sometimes be a bit weird.

        In the unittest framework, some assertions need to be used a context handlers that wrap the function under test.
        This is mainly true for things that need to capture side effects, like raising exceptions or writing to logs.
        """
        game_100_game.PLAYER_AMOUNT = 2
        game_100_game.CURRENT_PLAYER = "Player 1"
        mock_input.return_value = "not a digit"

        with self.assertRaises(TypeError):
            game_100_game.player()


if __name__ == '__main__':
    unittest.main()
