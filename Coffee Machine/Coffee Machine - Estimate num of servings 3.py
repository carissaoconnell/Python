ONE_CUP_NEEDED_WATER_AMOUNT = 200  # ml
ONE_CUP_NEEDED_MILK_AMOUNT = 50  # ml
ONE_CUP_NEEDED_COFFEE_AMOUNT = 15  # g


def get_available_coffee_cups_amount(water, milk, coffee):
    return min(
        water // ONE_CUP_NEEDED_WATER_AMOUNT,
        milk // ONE_CUP_NEEDED_MILK_AMOUNT,
        coffee // ONE_CUP_NEEDED_COFFEE_AMOUNT,
    )


def get_answer_to_coffee_request(cups_number, available_cups):
    if cups_number > available_cups:
        return f"No, I can make only {available_cups} cups of coffee"

    extra_cups_amount = available_cups - cups_number

    if extra_cups_amount:
        return f"Yes, I can make that amount of coffee " \
               f"(and even {extra_cups_amount} more than that)"

    return "Yes, I can make that amount of coffee"


def main():
    available_cups_amount = get_available_coffee_cups_amount(
        int(input("Write how many ml of water the coffee machine has:")),
        int(input("Write how many ml of milk the coffee machine has:")),
        int(input("Write how many grams of coffee beans the coffee machine has:")),
    )

    print(
        get_answer_to_coffee_request(
            int(input("Write how many cups of coffee you will need:")),
            available_cups_amount,
        )
    )


if __name__ == '__main__':
    main()
