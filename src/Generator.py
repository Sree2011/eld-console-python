class Generator:
    def __init__(self,gen_id,min_capacity,max_capacity,a,b,c):
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
        if (power < self.min_capacity):
            return self.min_capacity
        elif (power > self.max_capacity):
            return self.max_capacity
        else:
            return power
        
    

