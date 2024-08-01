# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """
import winsound

from EnigmaView import EnigmaView
from enigmaRotor import EnigmaRotor
from EnigmaConstants import ROTOR_PERMUTATIONS, REFLECTOR_PERMUTATION


class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self.__views = []
        self.__key_status = {chr(key): False for key in range(ord('A'), ord('Z') + 1)}
        self.__lamp_status = {chr(lamp): False for lamp in range(ord('A'), ord('Z') + 1)}
        self.__rotors = [EnigmaRotor(permutation) for permutation in ROTOR_PERMUTATIONS]

    def add_view(self, view):
        """Adds a view to this model."""
        self.__views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self.__views:
            view.update()

    def is_key_down(self, letter):
        return self.__key_status[letter]

    def is_lamp_on(self, letter):
        return self.__lamp_status[letter]

    def key_pressed(self, letter):
        self.__key_status[letter] = True
        self.advance_rotors()
        letter = self.__encrypt(letter)
        self.__lamp_status[letter] = True
        self.update()


    def key_released(self, letter):
        self.__key_status[letter] = False
        letter = self.__encrypt(letter)
        self.__lamp_status[letter] = False
        self.update()

    def get_rotor_letter(self, index):
        rotor = self.__rotors[index]
        letter = chr(ord('A') + rotor.get_offset())
        return letter

    def rotor_clicked(self, index):
        self.__rotors[index].advance()
        self.update()

    def advance_rotors(self):
        for rotor in reversed(self.__rotors):
            carry = rotor.advance()
            if not carry:
                break

    def __encrypt(self, letter):

        for rotor in reversed(self.__rotors):
            letter = rotor.forward_encryption(letter)

        letter = self.apply_reflector(letter)

        for rotor in self.__rotors:
            letter = rotor.backward_encryption(letter)

        return letter

    def apply_reflector(self, letter):
        index = ord(letter) - ord('A')
        letter = REFLECTOR_PERMUTATION[index]
        return letter


def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
