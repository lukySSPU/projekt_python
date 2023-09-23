
GRAVITY_CONSTANT = 6.67430e-11

SPEED_OF_LIGHT = 299792458

PLANCK_CONSTANT = 6.62607015e-34

BOLTZMANN_CONSTANT = 1.380649e-23

def calculate_gravitational_force(mass1, mass2, distance):
    force = GRAVITY_CONSTANT * (mass1 * mass2) / (distance ** 2)
    return force

def calculate_energy_wavelength(energy):
    wavelength = PLANCK_CONSTANT / (energy * SPEED_OF_LIGHT)
    return wavelength

def calculate_temperature_energy(temperature):
    energy = 3/2 * BOLTZMANN_CONSTANT * temperature
    return energy
