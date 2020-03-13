from .. import Provider as BankProvider


class Provider(BankProvider):
    bban_format = '#'*5 + '?'*12
    country_code = 'CH'
