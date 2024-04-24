from membership import Membership
from bank_account import BanckAccount

class User():
    def __init__(self,name: str, alias: str, password: str, bank_account: BanckAccount):
        self.name = name
        self.alias = alias
        self.password = password
        self.bank_account= bank_account
        self.grants = None
        self.membership = Membership('Free')
    
    
    @staticmethod
    def login(username: str, password: str):
        """
        This is static method used by users
        """
    def can_publish():

class Player(User):
    """This is a class player"""
    def __init__(self, age: int, name: str, alias: str, password: str, bank_account: BanckAccount):
        super().__init__(name, alias, password, bank_account)
        self.age = age
        self.bought_vidogames = []
    
    def buy_videogame(code):
        videogame = Catalog.get_videogame(code)
        self.bougth_videogames.append(videogame)

class Seller(User):
    def __init__(self,reputation: dict, name: str, alias: str, password: str, bank_account: BanckAccount):
        super().__init__(name, alias, password, bank_account)
        self.reputation = reputation
    
    def publish_videogame(videogame: VideoGame):bool
    pass



class Manager(User):
    def register_news(news: News):
        """xdxdxd
        """
        # TODO: up to db

    def deactivate_news(news: News):
        # TODO: up to db
