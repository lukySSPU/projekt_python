from physics import GRAVITY_CONSTANT, calculate_gravitational_force, calculate_energy_wavelength, calculate_temperature_energy

mass1 = 5.0
mass2 = 10.0
distance = 2.0

force = calculate_gravitational_force(mass1, mass2, distance)
print(f"Gravitational force between objects: {force} N")

energy = 3.0e-19
wavelength = calculate_energy_wavelength(energy)
print(f"Wavelength of a photon with energy {energy} J: {wavelength} m")

temperature = 300.0
avg_energy = calculate_temperature_energy(temperature)
print(f"Average kinetic energy of gas particles at {temperature} K: {avg_energy} J")
