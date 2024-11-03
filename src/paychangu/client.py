import requests
from .models.payment import Payment
from .models.payout import Payout
from .utils.http import handle_response

class PayChanguClient:
    BASE_URL = "https://api.paychangu.com"

    def __init__(self, secret_key):
        self.secret_key = secret_key
        self.headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.secret_key}",
        }
        self.payout_service = self.PayoutService(self)
        self.airtime_service = self.AirtimeService(self)
        self.direct_charge_service = self.DirectChargeService(self)

    def initiate_transaction(self, payment: Payment):
        url = f"{self.BASE_URL}/payment"
        payload = payment.to_dict()
        response = requests.post(url, json=payload, headers=self.headers)
        return handle_response(response)

    def verify_transaction(self, tx_ref: str):
        url = f"{self.BASE_URL}/verify-payment/{tx_ref}"
        response = requests.get(url, headers=self.headers)
        return handle_response(response)

    class PayoutService:
        def __init__(self, client):
            self.client = client

        def get_operators(self):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response)

        def initiate_payout(self, payout: Payout):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/payouts/initialize"
            payload = payout.to_dict()
            response = requests.post(url, json=payload, headers=self.client.headers)
            return handle_response(response)

        def fetch_transfer(self, charge_id: str):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/payments/{charge_id}/details"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response)

    class AirtimeService:
        def __init__(self, client):
            self.client = client

        def get_operators(self):
            url = f"{PayChanguClient.BASE_URL}/bill_payment/get-operators"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response)

        def create_bill(self, amount: int, phone_number: str, operator_id: str):
            url = f"{PayChanguClient.BASE_URL}/bill_payment/create"
            payload = {
                "amount": amount,
                "phone_number": phone_number,
                "operator_id": operator_id,
            }
            response = requests.post(url, json=payload, headers=self.client.headers)
            return handle_response(response)

    class DirectChargeService:
        def __init__(self, client):
            self.client = client

        def get_supported_operators(self):
            url = f"{PayChanguClient.BASE_URL}/mobile-money"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response)

        def initialize_payment(self, mobile: str, mobile_money_operator_ref_id: str, amount: str, charge_id: str, email: str = None, first_name: str = None, last_name: str = None):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/payments/initialize"
            payload = {
                "mobile": mobile,
                "mobile_money_operator_ref_id": mobile_money_operator_ref_id,
                "amount": amount,
                "charge_id": charge_id,
                "email": email,
                "first_name": first_name,
                "last_name": last_name,
            }
            response = requests.post(url, json=payload, headers=self.client.headers)
            return handle_response(response)

        def verify_charge(self, charge_id: str):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/payments/{charge_id}/verify"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response)

        def get_charge_details(self, charge_id: str):
            url = f"{PayChanguClient.BASE_URL}/mobile-money/payments/{charge_id}/details"
            response = requests.get(url, headers=self.client.headers)
            return handle_response(response) 