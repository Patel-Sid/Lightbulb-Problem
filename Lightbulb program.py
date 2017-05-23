class LightSwitch:
    '''A class to represent a light switch
    '''
    def __init__(self, state):
        '''(LightSwitch, str) -> NoneType
        REQ: State should be either "on" or "off"
        This method is used to initialize the state of the switch
        '''
        # If the switch is off then store it as False boolean type
        if self._state == "off":
            self._state = False
        # If the switch is on then store it as True boolean type
        elif self._state == "on":
            self._state = True

    def turn_on(self):
        '''(LightSwitch) -> NoneType
        This method is used to turn on a switch
        '''
        # If the switch is already on then do nothing
        if self._state is not True:
            self._state = True

    def turn_off(self):
        '''(LightSwitch) -> NoneType
        This method is used to turn off a switch
        '''
        # If the switch is already off then do nothing
        if self._state is not False:
            self._state = False

    def flip(self):
        '''(LightSwitch) -> NoneType
        This method is used to flip a switch
        '''
        # If the switch is off then turn it on, and if the switch is on turn
        # it off
        self._state = not(self._state)

    def __str__(self):
        '''(LightSwitch) -> str
        This method will return a string stating whether a switch is "on" or
        "off" when the user prints LightSwitch
        '''
        # If the user prints a switch, it will print accordingly to the current
        # state of the switch
        if self._state is True:
            self._newstate = "on"
        elif self._state is False:
            self._newstate = "off"
        return "I am " + (self._newstate)


class SwitchBoard:
    '''This class is used to represent a Switchboard made of up n switches
    '''
    def __init__(self, number_of_switches):
        '''(SwitchBoard, int) -> NoneType
        REQ: Number of switches must be greater than 0
        This method initializes the state of all the switches in the
        SwitchBoard to "off"
        '''
        self._number_of_switches = number_of_switches
        # Create an empty list to store the state of all the switches
        my_list = []
        # Loop through every switch in the SwitchBoard
        for i in range(self._number_of_switches):
            # Turn every switch to "off" state
            my_list.append(False)
        self._number_of_switches = my_list

    def which_switch(self):
        '''(SwitchBoard) -> list of int
        This method will return a list of integers representing the switches
        that are currently "on", in order
        '''
        # Create an empty list
        my_list = []
        # Loop through every switch in the SwitchBoard
        for i in range(len(self._number_of_switches)):
            if (self._number_of_switches[i] == True):
                # Only add switches to the list if they are in "on" state
                my_list.append(i)
        return my_list

    def flip(self, switch_to_flip):
        '''(SwitchBoard) -> NoneType
        This method will flip the state of the n'th lightswitch
        REQ: The switch must belong to the SwitchBoard
        '''
        # Checks if the switch is in SwitchBoard
        if switch_to_flip in range(len(self._number_of_switches)):
            # If it is then save its index value
            index = self._number_of_switches[switch_to_flip]
            # If the switch is on then turn it off
            if index is True:
                self._number_of_switches[switch_to_flip] = False
            # Otherwise the switch is off, hence turn the switch on
            else:
                self._number_of_switches[switch_to_flip] = True

    def flip_every(self, switch_to_flip):
        '''(SwitchBoard) -> NoneType
        This method will flip every the state of every n'th lightswitch
        starting with the integer 0
        REQ: The switch must belong to the SwitchBoard
        '''
        # If the user want's to flip every n'th switch, then starting at 0
        # flip every n'th switch
        if switch_to_flip > 0:
            for i in range(0, len(self._number_of_switches), switch_to_flip):
                SwitchBoard.flip(self, i)

    def __str__(self):
        '''(SwitchBoard) -> str
        This method will state which switches are currently "on" when the user
        prints SwitchBoard
        '''
        my_switches = "The following switches are on:"
        # Loop through every switch in the SwitchBoard and if it is"on" add
        # it to the statement
        for i in range(len(self._number_of_switches)):
            if (self._number_of_switches[i] == True):
                my_switches += " " + str(i)
        return my_switches

    def reset(self):
        '''(SwitchBoard) -> NoneType
        This method is used to turn off all the switches, regardless of their
        current state
        '''
        # Find out how many switches we have to turn "off" in the SwitchBoard
        number_of_switches = (len(self._number_of_switches))
        # Call the method which initializes the state of all switches to "off"
        SwitchBoard.__init__(self, number_of_switches)

# SOVE THE LOGIC PUZZLE
# This code will only run if the file is not imported
if(__name__ == "__main__"):
    # Create a SwitchBoard with switches starting from 0,1,2,...,1023
    any_switchboard = SwitchBoard(1024)
    # Loop through all the switches
    for i in range(1, 1024):
        # Flip the state of every n'th switch
        SwitchBoard.flip_every(any_switchboard, i)
    # Show which switches are on
    print(any_switchboard)
