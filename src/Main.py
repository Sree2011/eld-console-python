import Generator
import InputLoader
import ELDCalculator

def main():
    use_csv = True  # Toggle this to True to load from CSV
    input = InputLoader.InputLoader()

    if use_csv:
        file_path = "./input/10-generator_system.csv"
        input.load_data_from_file(file_path)
    else:
        input.load_data_from_user()

    gen_list = input.get_generators()
    
    if not gen_list:
        print("No valid generators loaded. Exiting.")
        return

    print(f"Total generators loaded: {len(gen_list)}")

    # Print generator details
    input.display_generators()

    total_demand = 2000.0
    eld_calculator = ELDCalculator.ELDCalculator(len(gen_list), gen_list, total_demand)

    el_dispatch = eld_calculator.lambda_iteration()
    for i, power in enumerate(el_dispatch):
        print(f"Generator {i + 1} dispatched power: {power:.3f} kW")

if __name__ == "__main__":
    main()