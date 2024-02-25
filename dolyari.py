class CurrencyConverter:
    def __init__(self, usd_exchange_rate):
        self.usd_exchange_rate = usd_exchange_rate

    def convert_to_usd(self, amount):
        return amount * self.usd_exchange_rate

try:
    usd_exchange_rate = 0.26

    converter = CurrencyConverter(usd_exchange_rate)

    amount_in_local_currency = float(input("Введіть кількість гривень: "))
    usd_amount = converter.convert_to_usd(amount_in_local_currency)
    print("Відповідна сума в доларах США: {:.2f}".format(usd_amount))
except ValueError:
    print("Будь ласка, введіть числове значення.")
