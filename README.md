# PayChangu SDK for Python

A powerful and easy-to-use Python SDK for integrating PayChangu payment services into your applications. This SDK provides seamless access to PayChangu's suite of payment solutions including Mobile Money payments, payouts, airtime purchases, and direct charges.

## Features

- Mobile Money Payments
- Mobile Money Payouts 
- Airtime Purchase
- Direct Mobile Money Charges
- Simple API Integration
- Comprehensive Error Handling
- Type Hints Support
- Python 3.7+ Compatible

## Installation

You can install the PayChangu SDK using pip:

```bash
pip install paychangu
```

## Usage

To use the PayChangu SDK, you need to create an instance of the `PayChanguClient` class with your secret key:

```python
from paychangu import PayChanguClient

client = PayChanguClient(secret_key="your_secret_key")
```

### Level

#### Initiate a Transaction

```python
from paychangu.models.payment import Payment
payment = Payment(
    amount=100,
    currency="MWK",
    email="user@example.com",
    first_name="John",
    last_name="Doe",
    callback_url="https://example.com/callback",
    return_url="https://example.com/return",
    tx_ref="unique_transaction_reference",
    customization={
        "title": "Test Payment",
        "description": "Payment Description",
    },
    meta={
        "uuid": "uuid",
        "response": "Response",
    },
)
response = client.initiate_transaction(payment)
print(response)
```


#### Verify a Transaction

```python
tx_ref = "unique_transaction_reference"
response = client.verify_transaction(tx_ref)
print(response)
```

### Payout

#### Get Payout Operators

```python
operators = client.payout_service.get_operators()
print(operators)
```

#### Initiate a Payout

```python
from paychangu.models.payout import Payout
payout = Payout(
amount=100,
currency="MWK",
mobile_number="1234567890",
network="TNM",
reference="unique_payout_reference",
callback_url="https://example.com/callback",
)
response = client.payout_service.initiate_payout(payout)
print(response)
```

#### Fetch Transfer Details

```python
charge_id = "jvivuiviu"
response = client.payout_service.fetch_transfer(charge_id)
print(response)
```


### Airtime

#### Get Airtime Operators

```python
operators = client.airtime_service.get_operators()
print(operators)
```

#### Create an Airtime Bill

```python
amount = 100
phone_number = "1234567890"
operator_id = "airtel"
response = client.airtime_service.create_bill(amount, phone_number, operator_id)
print(response)
```

### Direct Charge MoMo

#### Get Supported Operators

```python
operators = client.direct_charge_service.get_supported_operators()
print(operators)
```

#### Initialize a Direct Charge

```python
amount = 100
currency = "MWK"
mobile_number = "1234567890"
network = "airtel"
reference = "unique_payment_reference"
response = client.direct_charge_service.initialize_payment(amount, currency, mobile_number, network, reference)
print(response)
```

#### Verify a Direct Charge

```python
charge_id = "charge_id_from_initialize_payment_response"
response = client.direct_charge_service.verify_charge(charge_id)
print(response)
```

#### Get Charge Details

```python
charge_id = "charge_id_from_initialize_payment_response"
response = client.direct_charge_service.get_charge_details(charge_id)
print(response)
```

## Support

For support, email support@paychangu.com or visit our [support page](https://paychangu.com/support).