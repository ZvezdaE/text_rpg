
class item_base():
    def __init__(self, name: str,  **kwargs : bool) -> None:
        self.title = name
        self.can_be_weapon = kwargs['weapon']
        self.can_throw = kwargs['throw']
        self.can_pick_up = kwargs['pick_up']
        self.can_push = kwargs['push']
        self.can_pull = kwargs['pull']
        self.in_inventory = kwargs['inventory']

    def __str__(self) -> str:
        return self.title

    def set_attribute(self, **kwargs) -> None:
        self.can_be_weapon = kwargs['weapon']
        self.can_throw = kwargs['throw']
        self.can_pick_up = kwargs['pick_up']
        self.can_push = kwargs['push']
        self.can_pull = kwargs['pull']
        self.in_inventory = kwargs['inventory']
    
    def set_weapon(self, status: bool) -> None:
        self.can_be_weapon = status

    def set_throw(self, status: bool) -> None:
        self.can_throw = status

    def set_push(self, status: bool) -> None:
        self.can_push = status

    def set_pull(self, status: bool) -> None:
        self.can_pull = status

    def set_in_inventory(self, status: bool) -> None:
        self.in_inventory = status

    def get_title(self) -> str:
        return self.title
    
    def get_weapon(self) -> bool:
        return self.can_be_weapon
    
    def get_throw(self) -> bool:
        return self.can_throw
    
    def get_push(self) -> bool:
        return self.can_push
    
    def get_pull(self) -> bool:
        return self.can_pull
    
    def get_in_inventory(self) -> bool:
        return self.in_inventory