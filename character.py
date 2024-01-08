

class character():
    
    def __init__(self, name: str, id: int = 0, inv_size: int = 5) -> None:
        self.id = id
        self.name = name
        self.experience = 0
        self.health = 100
        self.inventory_size = inv_size
        
    def get_name(self) -> str:
        return self.name
    
    def get_exp(self) -> int:
        return self.experience
    
    def get_health(self) -> int:
        return self.health
    
    def get_inv_size(self) -> int:
        return self.inventory_size
    
    def add_exp(self, exp_mod: int) -> None:
        self.experience += exp_mod

    def change_health(self, health_mod: int) -> None:
        self.health += health_mod

    def set_name(self, name: str) -> None:
        self.name = name

    def change_inv_size(self, inv_change: int = 0) -> None:
        self.inventory_size += inv_change