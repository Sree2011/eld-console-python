<script src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script> 
<script type="module"> 
    Array.from(document.getElementsByClassName("language-mermaid")).forEach(el => { el.classList.add("mermaid"); }); 
    import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11.4.1/dist/mermaid.esm.min.mjs'; 
    mermaid.initialize({ startOnLoad: true, theme: 'light' }); 
</script>

# eld-console-python
Economic Load Dispatch console based application using python


# Code documentation
1. [main-doc](https://sree2011.github.io/eld-console-main-doc/)
2. [java](https://sree2011.github.io/eld-console-java/)


# Python documentation

1. [Generator](./docs/src/Generator.html)
2. [InputLoader](./docs/src/InputLoader.html)
3. [ELDCalculator](./docs/src/ELDCalculator.html)
4. [Main](./docs/src/Main.html)


# Class Diagram

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


    Main -- ELDCalculator : uses
    Main -- InputLoader : uses
    Main -- Generator : uses
    InputLoader -- Generator : uses
end

```


# References
[1] Power System Analysis by Hadi Saadat, 2010 edition
[2] IEEE 10-generator bus system