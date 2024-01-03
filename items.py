
class item_base():
    def __init__(self, name: str,  **kwargs : bool) -> None:
        self.title = name
        self.can_be_weapon = kwargs['weapon']
        self.can_throw = kwargs['throw']
        self.pick_up = kwargs['pick_up']
        self.push = kwargs['push']
        self.pull = kwargs['pull']
        self.in_inventory = kwargs['inventory']

    def __str__(self) -> str:
        return self.title

    def set_attribute(self, **kwargs) -> None:
        self.can_be_weapon = kwargs['weapon']
        self.can_throw = kwargs['throw']
        self.pick_up = kwargs['pick_up']
        self.push = kwargs['push']
        self.pull = kwargs['pull']
        self.in_inventory = kwargs['inventory']
    
    def get_title(self) -> str:
        return self.title
    
    def get_weapon(self) -> bool:
        return self.can_be_weapon
    
    def get_throw(self) -> bool:
        return self.can_throw
    
    def get_push(self) -> bool:
        return self.push
    
    def get_pull(self) -> bool:
        return self.pull
    
    def get_in_inventory(self) -> bool:
        return self.in_inventory