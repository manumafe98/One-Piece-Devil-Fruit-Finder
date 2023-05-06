import numpy as np

array = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
GAME_IS_ON = True
COUNT = 0


class TicTacToe:
    """Generate a class of the famous Tic Tac Toe game
    """
    def print_chart(self, input_array):
        """Prints the chart in the console with the corresponding progress.
        Args:
            input_array (array): bidimensional array that represents the game chart
        """
        chart = f"""
         {input_array[0, 0]} | {input_array[0, 1]} | {input_array[0, 2]} 
        -----------
         {input_array[1, 0]} | {input_array[1, 1]} | {input_array[1, 2]}
        -----------
         {input_array[2, 0]} | {input_array[2, 1]} | {input_array[2, 2]}      
        """
        print(chart)

    def is_position_valid(self, input_array, input_row, input_col):
        """Checks if the position the player is entering is valid or is already taken.

        Args:
            input_array (array): bidimensional array that represents the game chart
            input_row (int): The row where you want to place your character
            input_col (int): The column where you want to place your character

        Returns:
            boolean: Returns true or false depending if the position is taken.
        """
        if input_array[input_row, input_col] == "X" or array[input_row, input_col] == "O":
            return False
        return True

    def check_win(self, input_array):
        """Check if the winning conditions of the game are matched.

        Args:
            input_array (array): bidimensional array that represents the game chart

        Returns:
            null: Returns None until there is a winner.
        """
        # Check rows
        for rows in range(3):
            if input_array[rows, 0] == input_array[rows, 1] == input_array[rows, 2] != " ":
                return input_array[rows, 0]

        # Check columns
        for cols in range(3):
            if input_array[0, cols] == input_array[1, cols] == input_array[2, cols] != " ":
                return input_array[0, cols]

        # Check diagonals
        if input_array[0, 0] == input_array[1, 1] == input_array[2, 2] != " ":
            return input_array[0, 0]
        if input_array[0, 2] == input_array[1, 1] == input_array[2, 0] != " ":
            return input_array[0, 2]

        return None


while GAME_IS_ON:
    tic_tac_toe = TicTacToe()

    tic_tac_toe.print_chart(array)

    if " " not in array:
        # Checks for blank spaces in the array and if there are not.
        # And there is no winner already its a tie.
        print("It's a tie!")
        GAME_IS_ON = False
        break

    if COUNT % 2 == 0:
        # Indicates which player should play.
        PLAYER = "X"
    else:
        PLAYER = "O"

    POSITION_VALID = False
    while not POSITION_VALID:
        position = input(f"{PLAYER} turn, enter the row and column: ")
        row, col = int(position[0]), int(position[1])
        if tic_tac_toe.is_position_valid(array, row, col):
            array[row, col] = PLAYER
            POSITION_VALID = True
        else:
            print("Please enter a valid position. That one is already occupied.")

    winner = tic_tac_toe.check_win(array)
    if winner:
        tic_tac_toe.print_chart(array)
        print(f"{winner} wins!")
        GAME_IS_ON = False

    COUNT += 1
