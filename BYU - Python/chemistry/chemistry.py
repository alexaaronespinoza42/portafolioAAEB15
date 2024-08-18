from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1

# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def make_periodic_table():
    periodic_table_dict = {
        # symbol: [name, atomic_mass]
        "Ac": ["Actinium", 227],
        "Ag": ["Silver", 107.8682],
        "Al": ["Aluminum", 26.9815386],
        # Add more elements to the dictionary
    }
    return periodic_table_dict

def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    total_molar_mass = 0
    for symbol_quantity in symbol_quantity_list:
        symbol = symbol_quantity[SYMBOL_INDEX]
        quantity = symbol_quantity[QUANTITY_INDEX]
        atomic_mass = periodic_table_dict[symbol][ATOMIC_MASS_INDEX]
        total_molar_mass += atomic_mass * quantity
    return total_molar_mass

def main():
    chemical_formula = input("Enter the molecular formula of the sample: ")
    sample_mass = float(input("Enter the mass in grams of the sample: "))

    periodic_table = make_periodic_table()
    symbol_quantity_list = parse_formula(chemical_formula)
    molar_mass = compute_molar_mass(symbol_quantity_list, periodic_table)
    number_of_moles = sample_mass / molar_mass

    print("Molar mass:", molar_mass, "grams/mole")
    print("Number of moles:", number_of_moles, "moles")

if __name__ == "__main__":
    main()