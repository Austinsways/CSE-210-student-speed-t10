from game import constants
from game.actor import Actor
from game.point import Point
import random as r

class Words:
    """A words floating across the screen, that the player can type, as well as the buffer for the play for the player to input
    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (word): An instance of word.
        """
        super().__init__()
        

        self._words = []
        self._segments = []
        self._inputs = []
        self._input_seg = []
        self._prepare()

    def _prepare(self):
        for i in range(0,5):
            temp_word = constants.LIBRARY[r.randint(0, 9999)]
            self._words.append(temp_word)
        self.create_segments()
    

    def move_word(self):
        """update the segments to cause them to move across the screen"""
        for segment in self._segments:
            segment.move_next()

    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments

    

    def _add_segment(self, text, position, velocity):
        """takes the characters in the word and creates a segment
        Args:
            self (Word): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)
    
    def get_last_input(self):
        """Returns the last input stored in self._inputs.
        
        Args:
            self (Words): An instance of Words.
        """
        return self._inputs[-1]

    def update_words(self, index):
        """delete the typed word and add a new word to the list"""
        self._words[index] = constants.LIBRARY(r.randint(0,9999))
        self.create_segments()

        pass

    def create_segments(self):
        self._segments = []
        for word in self._words:
            x = r.randint(1, constants.MAX_X - 2)
            y = r.randint(1, constants.MAX_Y - 2)
            l = 0
            for letter in word:
                text = letter
                position = Point(x + l, y)
                velocity = Point(1, 0)
                self._add_segment(text, position, velocity)
                l += 1

    def _compare(self):
        input_string = ""
        for character in self._inputs:
            input_string = input_string + character
        i = 0
        for word in self._words:
            if word in input_string:
                self.update_words(i)
                return 1
            i += 1
        return 0

    def reset_inputs(self):
        self._inputs.clear() 