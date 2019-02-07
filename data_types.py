from copy import copy
from collections import OrderedDict, Counter, namedtuple


def some_collctions():
    # Remembers the order the keys are added!
    x = OrderedDict(a=1, b=2, c=3)
    # Counts the frequency of each character
    y = Counter("Hello World!")


def example_namedtuple():
    """Namedtuples example"""
    Room = namedtuple('Room', ['room_size', 'price', 'sunlight', 'flat_rooms'])

    flat = Room(30, 600, True, 3)

    if flat.price <= 620:
        print('take it!')


def get_me_rule():
    rule = {}
    rule['param1'] = "first setting"
    rule['param2'] = "second setting"
    return rule


def list_output_without_copy(wrapped_rule, date_ranges):
    list_wrapped_rules = []
    for date_range in date_ranges:
        wrapped_rule['date_range'] = date_range
        list_wrapped_rules.append(wrapped_rule)
    return list_wrapped_rules


def list_output_with_copy(wrapped_rule, date_ranges):
    list_wrapped_rules = []
    for date_range in date_ranges:

        new_wrapped_rule = copy(wrapped_rule)

        # messing up with the deeper level object, even old object before copy will be affected
        new_wrapped_rule['rules']['param1'] = 'wrong setting'

        # here will be only copy affected
        new_wrapped_rule['new_key'] = 'only copy affected'

        new_wrapped_rule['date_range'] = date_range
        list_wrapped_rules.append(new_wrapped_rule)
    return list_wrapped_rules


def test_shallow_copy():
    rule = get_me_rule()

    date_ranges = [{'from': '2018-01-05', 'to': '2018-03-22'}, {'from': '2018-04-05', 'to': '2018-07-22'}]

    list_wrapped_rules = []

    wrapped_rule = {"rules": rule, "source": 'internet', "date_range": None}

    # Correct
    print("List output with copy:")
    print(list_output_with_copy(wrapped_rule, date_ranges))

    # Both wrapped rules with the same date range
    print("List output without copy: (problem - rewriting the same object in array - the same date range)")
    print(list_output_without_copy(wrapped_rule, date_ranges))



if __name__ == "__main__":
    test_shallow_copy()
