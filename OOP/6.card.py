class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name: str, password: str, payment_limit: int) -> None:
        self.set_name(name)
        self.set_password(password)
        self.set_payment_limit(payment_limit)
    
    def get_name(self):
        return self.__name
    def get_password(self)-> str:
        return "비밀 번호는 볼 수 없습니다"
    def get_payment_limit(self)-> str:
        return self.__payment_limit
    def set_name(self, name: str)-> None:
        self.__name = name
    def set_password(self, password: str)-> None:
        self.__password = password
    def set_payment_limit(self, payment_limit: int):
        if 0 < payment_limit < self.MAX_PAYMENT_LIMIT:
            self.__payment_limit = payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해 주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())

card.set_name("성태호")
card.set_password("1234")
card.set_payment_limit(-10)

print(card.get_name())
print(card.get_password())
print(card.get_payment_limit())