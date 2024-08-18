import math

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    v = fluid_velocity
    n = quantity_fittings
    return (-0.04 * 998.2 * v**2 * n) / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity):
    d = hydraulic_diameter
    v = fluid_velocity
    return (998.2 * d * v) / 0.0010016

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k = 0.1 + (50 / reynolds_number) * (larger_diameter / smaller_diameter)**4 - 1
    v = fluid_velocity
    return -k * 998.2 * v**2 / 2000

def water_column_height(tower_height, tank_height):
    return tower_height + tank_height

def pressure_gain_from_water_height(water_height):
    return water_height * 9.80665 * 998.2 / 1000

def pressure_loss_from_pipe(diameter, length, friction_factor, velocity):
    friction_loss = friction_factor * (length / diameter) * (velocity**2) / (2 * 9.81)
    return friction_loss * 998.2 / 1000

PVC_SCHED80_INNER_DIAMETER = 0.28687  # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013   # (unitless)
SUPPLY_VELOCITY = 1.65                # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692  # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018    # (unitless)
HOUSEHOLD_VELOCITY = 1.75             # (meters / second)

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter, velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")

if __name__ == "__main__":
    main()