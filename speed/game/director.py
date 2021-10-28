from time import sleep
from game import constants
from game.score import Score
from game.words import Words

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        words (Words): An object of the Words class.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self.words = Words()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the typed letter and checks if it is valid.

        Args:
            self (Director): An instance of Director.
        """
        tested_input = self._input_service.get_letter()
        if tested_input == None:
            self._keep_playing = False
        elif tested_input == "":
            pass
        else:
            self.words._inputs.append(tested_input)
        self.words.move_word()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking last input value, reseting inputs, and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._update_points()
        if self.words.get_last_input() == "*":
            self.words.reset_inputs()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self.words.refresh()
        self._output_service.clear_screen()
        self._output_service.draw_actors(self.words.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.draw_actors(self.words.get_input_all())
        self._output_service.flush_buffer()
        


    def _update_points(self):
        self._score.add_points(self.words._compare())