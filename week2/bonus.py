from utils.csv_reader import import_csv_flat
from week1.bonus import ShipComputer
from unittest.mock import patch
from itertools import permutations


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
        def output_pause(x):
            if input := x.strip():
                # get print value and pause program
                self.output.append(int(input))
                self.program._quit = True

        # overide input and print in original program so we can capture values
        with patch('builtins.input', lambda:self.inputs.pop(0)), patch('sys.stdout.write', output_pause):
            self.program._quit = False
            self.program.execute()
        
        return self.output[-1]

    @property
    def done(self):
        # is program done or paused
        return self.program.codes[self.program._ptr] == 99


def run_amplifiers(data, phase_settings):
    amplifiers = [Amplifier(data.copy(), phase) for phase in phase_settings]

    # ready initial data
    amplifiers[0].inputs.append(0)

    # keep going until last amplifier has finished
    while not amplifiers[-1].done:
        for i in range(len(amplifiers)):
            # pipe amplifier outout into next amplifier
            amplifiers[(i+1) % len(amplifiers)].inputs.append(amplifiers[i].run())
    # final amplifier output        
    return amplifiers[-1].output[-1]

def bonus(phase_range):
    data = [int(x) for x in import_csv_flat("week2/bonus.csv")]
    phase_settings = list(permutations(phase_range))
    max_thrust = 0
    for phase in phase_settings:
        if (thrust := run_amplifiers(data,list(phase))) > max_thrust:
            max_thrust = thrust
    return max_thrust

def main():
    print("bonus 1: ", bonus(range(0, 5)))
    print("bonus 2: ", bonus(range(5, 10)))

if __name__ == "__main__":
    main()