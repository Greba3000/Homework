# Implement custom dictionary that will memorize 10 latest CHANGED keys.
# Using method "get_history" return this keys.

class HistoryDict:  # try HistoryDict(dict)

    def __init__(self, data_dict: dict):
        self.temp_dict = data_dict
        self.out = list()

    def set_value(self, new_key, new_value):
        self.temp_dict[new_key] = new_value
        if len(self.out) == 10:
            del self.out[0]
        else:
            self.out.append(new_key)

    def get_history(self) -> list:
        print(self.out)


if __name__ == "__main__":
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.set_value("bar2", 55)
    d.get_history()
