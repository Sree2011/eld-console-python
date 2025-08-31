class Generator:
    def __init__(self,gen_id,min_capacity,max_capacity,a,b,c):
        """
        Initialize a Generator object with its parameters.

        Parameters:
        -----------
            - `gen_id (str)`: The unique identifier for the generator.
            - `min_capacity (float)`: The minimum capacity of the generator.
            - `max_capacity (float)`:The maximum capacity of the generator.
            - `a (float)`: The quadratic cost coefficient.
            - `b (float)`: The linear cost coefficient.
            - `c (float)`: The constant cost coefficient.

        Returns:
        --------
        None

        """
        self.gen_id = gen_id
        self.min_capacity = min_capacity
        self.max_capacity = max_capacity
        self.a = a
        self.b = b
        self.c = c
    
    def calculate_cost(self,power):
        
        """
        Calculate the cost for a given power output.

        Parameters:
        -----------
        `power (float)`: 
            The power output of the generator.

        Returns:
        --------
        `float`: 
            The cost associated with the given power output.
        """

        return (self.a * (power * power) + (self.b * power) + self.c)
    

    def validate_power(self,power):
        """
        Validate if the given power is within the generator's capacity limits.
        Parameters:
        -----------
        `power (float)`: 
            The power output to validate.
        Returns:
        --------
        `float`: 
            The validated power output, adjusted to be within capacity limits if necessary.
        """
        if (power < self.min_capacity):
            return self.min_capacity
        elif (power > self.max_capacity):
            return self.max_capacity
        else:
            return power
        
    

