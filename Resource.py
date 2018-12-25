class Resource:
    def get_a_cost(self,base,mul,level):
        return base*mul**level

    def getMetalCost(self,level):
        return self.get_a_cost(self.metal_base_cost,
                        self.build_cost_multiplier,
                        level)
    def getCrystalCost(self,level):
        return self.get_a_cost(self.crystal_base_cost,
                               self.build_cost_multiplier,
                               level)
    def getProductaion(self, level):
           return self.production_multiplier * level * 1.1 ** level 

