class Metal(Resource):
    self.metal_base_cost = 60 
    self.crystal_base_cost = 15
    self.build_cost_multiplier = 1.5
    self.energy_cost_multiplier = 10
    self.production_multiplier = 30
                  

class Crystal(Resource):
    self.metal_base_cost = 48
    self.crystal_base_cost = 24
    self.build_cost_multiplier = 1.6
    self.energy_cost_multiplier = 10
    self.production_multiplier = 20


class Deuterium(Resource):
    self.metal_base_cost = 225
    self.crystal_base_cost = 75
    self.build_cost_multiplier = 1.5
    self.energy_cost_multiplier = 20
    self.production_multiplier = 20

class SolarFarm(Resource):
    self.metal_base_cost = 75
    self.crystal_base_cost = 30
    self.build_cost_multiplier = 1.5
    self.energy_cost_multiplier = 0
    self.production_multiplier = 20

