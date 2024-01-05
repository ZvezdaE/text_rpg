

class character():
    
    def __init__(self, name: str, id: int = 0, inv_size: int = 5) -> None:
        self.id = id
        self.name = name
        self.exp = 0
        self.health = 100
        self.inv_size = inv_size
        
    def get_name(self) -> str:
        return self.name
    
    def get_exp(self) -> int:
        return self.exp
    
    def get_health(self) -> int:
        return self.health
    
    def get_inv_size(self) -> int:
        return self.inv_size
    
    def add_exp(self, exp_mod: int) -> None:
        self.exp += exp_mod

    def change_health(self, health_mod: int) -> None:
        self.health += health_mod

    def set_name(self, name: str) -> None:
        self.name = name

    def change_inv_size(self, inv_change: int = 0) -> None:
        self.inv_size += inv_change