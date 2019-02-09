from copy import copy, deepcopy
from collections import OrderedDict, Counter, namedtuple


class CustomList:
    """
    This is all you need, to implement iterable list.
    """
    def __init__(self, *lst):
        self._lst = lst

    def __getitem__(self, item):
        return self._lst[item]


def example_some_collections():
    # Remembers the order of the added keys
    x = OrderedDict(a=1, b=2, c=3)
    # Counts the frequency of each character
    y = Counter("Hello World!")
    # Namedtuple example
    Flat = namedtuple('Flat', ['flat_size', 'price', 'sunlight', 'rooms'])
    flat = Flat(80, 600, True, 3)
    if flat.price <= 620:
        print('take it!')


def get_config():
    config = dict()
    config['order'] = ''
    return config


def list_output_without_copy(wrapped_setting, date_ranges):
    list_wrapped_settings = []
    for index, date_range in enumerate(date_ranges):
        wrapped_setting['config']['order'] = f'rule number {index}'
        wrapped_setting['date_range'] = date_range
        list_wrapped_settings.append(wrapped_setting)
    return list_wrapped_settings


def list_output_with_shallow_copy(wrapped_setting, date_ranges):
    list_wrapped_settings = []
    for index, date_range in enumerate(date_ranges):
        new_wrapped_setting = copy(wrapped_setting)
        new_wrapped_setting['config']['order'] = f'rule number {index}'
        new_wrapped_setting['date_range'] = date_range
        list_wrapped_settings.append(new_wrapped_setting)
    return list_wrapped_settings


def list_output_with_deep_copy(wrapped_setting, date_ranges):
    list_wrapped_settings = []
    for index, date_range in enumerate(date_ranges):
        new_wrapped_setting = deepcopy(wrapped_setting)
        new_wrapped_setting['config']['order'] = f'rule number {index}'
        new_wrapped_setting['date_range'] = date_range
        list_wrapped_settings.append(new_wrapped_setting)
    return list_wrapped_settings


def test_data_output():
    """
    Example of working with mutable data type - dict,
    
    In the first attempt we see, we update the same wrapper setting 2 times, so only the last update is preserved.
    In the final list then we have the same dict instance 2 times.
    
    In the second test with shallow copy, each wrapper setting is new dict instance, so the date range is updated
    for each one separately, but the inner config dict is in both settings the same. That's why you will get for both
    of them "order='rule number 1'" (only the last value).

    Only in the third example this all works correctly, because of the deepcopy. This means, that not only the
    wrapped setting will be new dict instance during the iteration, but also the inner config dict is always new dict.
    """
    config = get_config()
    date_ranges = [{'from': '2018-01-05', 'to': '2018-03-22'}, {'from': '2018-04-05', 'to': '2018-07-22'}]
    wrapped_settings = {"config": config, "source": 'internet', "date_range": None}

    print("List output without copy:")
    print(list_output_without_copy(wrapped_settings, date_ranges))

    print("List output using shallow copy:")
    print(list_output_with_shallow_copy(wrapped_settings, date_ranges))

    print("List output using deep copy:")
    print(list_output_with_deep_copy(wrapped_settings, date_ranges))


if __name__ == "__main__":
    test_data_output()
