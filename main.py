price = float(input())
vat = float(input())

try:
    vat_inclusive_price = round(price + (price * (vat/100)))
    print("VAT inclusive price:", vat_inclusive_price)
except ValueError:
    print("Invalid Input")
