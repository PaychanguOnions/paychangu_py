from typing import Optional

class Payment:
    def __init__(
        self,
        amount: int,
        currency: str,
        email: Optional[str],
        first_name: str,
        last_name: Optional[str],
        callback_url: str,
        return_url: str,
        tx_ref: str,
        customization: Optional[dict] = None,
        meta: Optional[dict] = None,
    ):
        self.amount = amount
        self.currency = currency
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.callback_url = callback_url
        self.return_url = return_url
        self.tx_ref = tx_ref
        self.customization = customization
        self.meta = meta

    def to_dict(self):
        return {
            "amount": self.amount,
            "currency": self.currency,
            "email": self.email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "callback_url": self.callback_url,
            "return_url": self.return_url,
            "tx_ref": self.tx_ref,
            "customization": self.customization,
            "meta": self.meta,
        } 