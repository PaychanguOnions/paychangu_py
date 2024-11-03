from typing import Optional

class Payout:
    def __init__(
        self,
        amount: int,
        currency: str,
        mobile_number: str,
        network: str,
        reference: str,
        callback_url: Optional[str] = None,
    ):
        self.amount = amount
        self.currency = currency
        self.mobile_number = mobile_number
        self.network = network
        self.reference = reference
        self.callback_url = callback_url

    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
            "mobile_number": self.mobile_number,
            "network": self.network,
            "reference": self.reference,
            "callback_url": self.callback_url,
        } 