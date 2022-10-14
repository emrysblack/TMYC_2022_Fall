from shared.santas_computer import ShipComputer
from unittest.mock import patch


class Amplifier():
    def __init__(self, data, phase_setting):
        self.program = ShipComputer(data)
        self.output = []
        self.inputs = [phase_setting]
    
    def run(self):
        """
        runs Santas Computer and pauses execution on output.
        a bit hacky to use test methods, 
        but we don't want to modify the original computer out of spec
        """
        def output_pause(input):
            # get print value and pause program
            self.output.append(input)
            self.program.quit = True

        # overide input and print in original program so we can capture values
        with patch('builtins.input', lambda:self.inputs.pop(0)), patch('builtins.print', output_pause):
            self.program.quit = False
            self.program.execute()
        
        return self.output[-1]

    @property
    def done(self):
        # is program done or paused
        return (ptr := self.program.ptr) > -1 and self.program.codes[ptr] == 99
