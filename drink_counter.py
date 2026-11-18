def drink_counter():
    try:
        balance = float(input("Money you have (number): €"))
        drink_price = float(input("Price of a drink (number): €"))
        refund_for_package = float(
            input("Amount of refund for each package (number): €")
        )
    except ValueError:
        print("Are yuo kidding?")
        return

    if refund_for_package >= drink_price and balance >= drink_price:
        print("You have lifetime subscription for that drink.")
        return

    count = 0
    while balance > drink_price:
        bought = balance // drink_price
        count += bought
        balance -= bought * (drink_price - refund_for_package)

    print(
        f"You can buy {int(count)} products and you will have €{balance:.2f} remaining"
    )


def main():
    drink_counter()


if __name__ == "__main__":
    main()
