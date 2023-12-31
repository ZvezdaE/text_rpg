

class character():
    
    def __init__(self, name: str, id: int = 0) -> None:
        self.id = id
        self.name = name
        self.exp = 0
        self.health = 100
        
    def get_name(self) -> str:
        return self.name
    
    def get_exp(self) -> int:
        return self.exp
    
    def get_health(self) -> int:
        return self.health
    
    def add_exp(self, exp_mod: int) -> None:
        self.exp += exp_mod

    def change_health(self, health_mod: int) -> None:
        self.health += health_mod

    def set_name
