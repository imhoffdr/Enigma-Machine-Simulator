# File: EnigmaModel.py

""" This is the starter file for the Enigma project. """

from EnigmaView import EnigmaView

class EnigmaModel:

    def __init__(self):
        """Creates a new EnigmaModel with no views."""
        self._views = [ ]
        self.key_status = {chr(key): False for key in range(ord('A'), ord('Z') + 1)}

    def add_view(self, view):
        """Adds a view to this model."""
        self._views.append(view)

    def update(self):
        """Sends an update request to all the views."""
        for view in self._views:
            view.update()

    def is_key_down(self, letter):
        return self.key_status[letter]

    def is_lamp_on(self, letter):
        return False        # In the stub version, lamps are always off

    def key_pressed(self, letter):
        self.key_status[letter] = True
        self.update()

    def key_released(self, letter):
        self.key_status[letter] = False
        self.update()

    def get_rotor_letter(self, index):
        return "A"          # In the stub version, all rotors are set to "A"

    def rotor_clicked(self, index):
        # You need to fill in this code
        self.update()

def enigma():
    """Runs the Enigma simulator."""
    model = EnigmaModel()
    view = EnigmaView(model)
    model.add_view(view)

# Startup code

if __name__ == "__main__":
    enigma()
