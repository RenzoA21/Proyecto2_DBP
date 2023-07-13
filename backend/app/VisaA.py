import json
import logging
import base64
from requests import Response
from visa_dps.VisaSession import VisaSession
from datetime import datetime
from typing import List


class Account:
    account_alias_id: str
    account_number: str
    account_type_code: str
    account_type_description: None
    institution_id: None
    account_indicator_code: None
    account_indicator_description: None
    balances: None
    is_funding: bool
    is_funding_computed: bool
    account_opened_date: datetime

    def __init__(self, account_alias_id: str, account_number: str, account_type_code: str, account_type_description: None, institution_id: None, account_indicator_code: None, account_indicator_description: None, balances: None, is_funding: bool, is_funding_computed: bool, account_opened_date: datetime) -> None:
        self.account_alias_id = account_alias_id
        self.account_number = account_number
        self.account_type_code = account_type_code
        self.account_type_description = account_type_description
        self.institution_id = institution_id
        self.account_indicator_code = account_indicator_code
        self.account_indicator_description = account_indicator_description
        self.balances = balances
        self.is_funding = is_funding
        self.is_funding_computed = is_funding_computed
        self.account_opened_date = account_opened_date


class Card:
    card_id: str
    pan: str
    accounts: List[Account]

    def __init__(self, card_id: str, pan: str, accounts: List[Account]) -> None:
        self.card_id = card_id
        self.pan = pan
        self.accounts = accounts
