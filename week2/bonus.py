from shared.csv_reader import read_flat as read_csv
from shared.amplifier import Amplifier
from itertools import permutations


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
    data = [int(x) for x in read_csv("week2/bonus.csv")]
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
