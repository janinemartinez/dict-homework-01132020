"""Print out all the melons in our inventory."""

from melons import *
# from melons import melon_names, melon_seedlessness, melon_prices


def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    melons_data = {}

    for number, melon_type in melon_names.items():

        melons_data[melon_type] = {'seedless': melon_seedlessness[number], 'price': melon_prices[number], 'flesh_color': None, 'weight': None, 'rind_color': None}

    for melon_type, melon_values in melons_data.items():
        print(melon_type)
        for melon_keys, melon_properties in melon_values.items():
            print(f"     {melon_keys}: {melon_properties}")






print_melon(melon_names, melon_prices, melon_seedlessness)



#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
