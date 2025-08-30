import Generator
import pandas as pd
from tabulate import tabulate
class InputLoader:
    def __init__(self):
        self.generators = []
        

    def load_data_from_user(self):
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
        print(tabulate(table, headers, tablefmt="grid"))
