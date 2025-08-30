class ELDCalculator:
    def __init__(self,gen_lambda,gen_array,num_generators):
        self.gen_lambda = 1
        self.gen_array = gen_array
        self.num_generators = num_generators
        self.tot_demand = 2000.0
        self.tolerance = 0.0001
        self.max_iterations = 10000
    
    def lambda_iteration(self):
        iteration = 0
        while iteration < self.max_iterations:
            P = []
            total_power = 0
            for gen in self.gen_array:
                power = (self.gen_lambda - gen.b) / (2 * gen.a)
                power = gen.validate_power(power)
                P.append(power)
                total_power += power
            
            if abs(total_power - self.tot_demand) <= self.tolerance:
                break
            
            if total_power < self.tot_demand:
                self.gen_lambda += 0.01
            else:
                self.gen_lambda -= 0.01
            
            iteration += 1
        
        return P, self.gen_lambda, iteration