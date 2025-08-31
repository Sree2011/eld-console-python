from . import Generator
import pandas as pd
from tabulate import tabulate
class InputLoader:
    """
    Class to load input data for generators.
    Can load data from user input or from a CSV file.
    
    Attributes:
    -----------
    `generators (list)`: List of Generator objects.
    
    Methods:
    --------
        - `load_data_from_user()`: Load generator data from user input.
        - `load_data_from_file(file_path)`: Load generator data from a CSV file.
        - `get_generators()`: Return the list of Generator objects.
        - `display_generators()`: Display the generator data in a tabular format.
    """

    def __init__(self):
        self.generators = []
        

    def load_data_from_user(self):
        """Load generator data from user input.
        Prompts the user to enter the number of generators and their details.
        
        Returns:
        --------
        None
        """

        num_generators = int(input("Enter the number of generators: "))
        for i in range(num_generators):
            print(f"Enter details for generator {i + 1}:")
            gen_id = input("  Generator ID: ")
            min_capacity = float(input("  Min Capacity: "))
            max_capacity = float(input("  Max Capacity: "))
            a = float(input("  Cost coefficient a: "))
            b = float(input("  Cost coefficient b: "))
            c = float(input("  Cost coefficient c: "))


            generator = Generator.Generator(gen_id, min_capacity, max_capacity, a, b, c)
            self.generators.append(generator)


    def load_data_from_file(self,file_path):
        """
        Load generator data from a CSV file.
        The CSV file should have the following columns:
        - Gen_ID
        - Min_Capacity
        - Max_Capacity
        - a
        - b
        - c
        
        Parameters:
        -----------
        `file_path (str)`: Path to the CSV file.

        Returns:
        --------
        None
        """
        data = pd.read_csv(file_path)
        for index, row in data.iterrows():
            gen_id = row['Gen_ID']
            min_capacity = row['Min_Capacity']
            max_capacity = row['Max_Capacity']
            a = row['a']
            b = row['b']
            c = row['c']
            generator = Generator.Generator(gen_id, min_capacity, max_capacity, a, b, c)
            self.generators.append(generator)

    def get_generators(self):
        return self.generators

    def display_generators(self):
        table = []
        for gen in self.generators:
            table.append([gen.gen_id, gen.min_capacity, gen.max_capacity, gen.a, gen.b, gen.c])
        headers = ["Gen_ID", "Min_Capacity", "Max_Capacity", "a", "b", "c"]
        df = pd.DataFrame(table, columns=headers)
        return df
