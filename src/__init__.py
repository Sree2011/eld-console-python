"""
Economic Load Dispatch (ELD) Module
----------------------------------


This module provides classes and functions to perform Economic Load Dispatch calculations
for a set of power generators based on their cost functions and operational constraints.


Classes:
--------

- Generator: Represents a power generator with its cost function and capacity limits.
- InputLoader: Loads generator data from user input or a CSV file.
- ELDCalculator: Performs the ELD calculation using the lambda iteration method.
- Main: The main script to run the ELD calculation and display results.


```mermaid
classDiagram
    class Generator {
        +gen_id: str
        +min_capacity: float
        +max_capacity: float
        +a: float
        +b: float
        +c: float
        +calculate_cost(power: float) -> float
        +validate_power(power: float) -> float
    }

    class InputLoader {
        +generators: List[Generator]
        +load_data_from_user() -> None
        +load_data_from_file(file_path: str) -> None
        +get_generators() -> List[Generator]
        +display_generators() -> pd.DataFrame
    }

    class ELDCalculator {
        +gen_lambda: float
        +gen_array: List[Generator]
        +num_generators: int
        +tot_demand: float
        +tolerance: float
        +max_iterations: int
        +lambda_iteration() -> Tuple[List[float], float, int]
    }

    class Main {
        +main() -> None
    }

Relationships:
    InputLoader "1" -- "many" Generator : contains
    ELDCalculator "1" -- "many" Generator : uses
    Main "1" -- "1" InputLoader : uses
    Main "1" -- "1" ELDCalculator : uses
"""