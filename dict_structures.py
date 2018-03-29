from copy import copy

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
        new_wrapped_rule['date_range'] = date_range
        list_wrapped_rules.append(new_wrapped_rule)
    return list_wrapped_rules

def test_object_change():
    rule = get_me_rule()

    date_ranges = [{'from': '2018-01-05', 'to': '2018-03-22'}, {'from': '2018-04-05', 'to': '2018-07-22'}]

    list_wrapped_rules = []

    wrapped_rule = {"rules": rule, "source": 'internet', "date_range": None}

    # Both wrapped rules with the same date range
    print("List output without copy: (problem - rewriting the same object in array - the same date range)")
    print(list_output_without_copy(wrapped_rule, date_ranges))

    print("List output with copy:")
    print(list_output_with_copy(wrapped_rule, date_ranges))


if __name__ == "__main__":
    test_object_change()
