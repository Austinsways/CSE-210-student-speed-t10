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
            self (Words): An instance of Words.
        """
        super().__init__()
        

        self._words = []
        self._segments = []
        self._inputs = []
        self._input_seg = []
        self.i = 0
        self.length = len(self._inputs)
        self._prepare()

    def _prepare(self):
        """Prepares the _words list by adding five words to the list.
        
        Args:
            self (Words): an instance of Words.
        """
        for i in range(0,5):
            temp_word = constants.LIBRARY[r.randint(0, 9999)]
            self._words.append(temp_word)
        self.create_segments()
    

    def move_word(self):
        """Update the segments to cause them to move across the screen
        
        Args:
            self (Words): an instance of Words.
        """
        for segment in self._segments:
            segment.move_next()

    def get_all(self):
        """Gets all the word segments.
        
        Args:
            self (Words): An instance of Words.

        Returns:
            list: The word segments.
        """
        return self._segments

    

    def _add_segment(self, text, position, velocity):
        """takes the characters in the word and creates a segment

        Args:
            self (Words): An instance of Words.
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
        if self.length != 0:
            return self._inputs[-1]
        else:
            return ""

    def update_words(self, index):
        """Delete the typed word and add a new word to the list
        
        Args:
            self (Words): an instance of Words.
            index: the index of the work in the _words list.
        """
        self._words[index] = constants.LIBRARY(r.randint(0,9999))
        self.create_segments()

        pass

    def create_segments(self):
        """Creates a list of actor objects to be displayed on the board
        
        Args:
            self (Words): an instance of Words.
        """
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
        """Compares what input has been received to the list of words
        
        Args:
            self (Words): an instance of Words.
        """
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

        """Clears _inputs list of any values
        
        Args:
            self (Words): an instance of Words.
        """

        self._inputs.clear()
        self._input_seg.clear()
        self.length = 0
        self.i = 0

    def _add_input_segment(self, text, position, velocity):
   
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._input_seg.append(segment)

    def get_input_all(self):
        return self._input_seg

    def refresh(self):            
        y = constants.MAX_Y
        v = Point(0,0)
        position = Point(self.i + 11, y)
        if not self.length == len(self._inputs):
            self._add_input_segment(self._inputs[-1], position, v)
            self.length += 1
            self.i += 1
