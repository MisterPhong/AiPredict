import datetime

class CryptoCoins:
    def __init__(self) -> None:
        self.coin_name: str
        self.date: datetime.date
        self.time: datetime.time
        self.current_price: float
        self.predicet_price: float
        self.actual_price: float
        self.create_at: datetime.date
        self.update_at: datetime.date
        self.next: CryptoCoins = None
