import json


class Matrix:
    def __init__(self):
        self.matrix = {}
        self.entry_list = []
        self.newest_entry = {}
        try:
            with open("matrix.json", mode="r") as data_file:
                self.matrix = json.load(data_file)
                self.entry_list = [item for item in self.matrix]
                print(self.entry_list)
        except FileNotFoundError:
            print("starting with new file")

    def add_new(self, entry):
        if entry not in self.entry_list:
            self.entry_list.append(entry)
            self.newest_entry = {
                entry: {item: "default" for item in self.entry_list}
            }
            self.matrix.update(self.newest_entry)
            # print(self.matrix)

            for dict_item in self.entry_list:
                if dict_item != entry:
                    self.matrix[dict_item][entry] = "default"
            print(self.matrix)

    def save(self):
        with open("matrix.json", mode="w") as data_file:
            json.dump(self.matrix, data_file)
            print("data saved")


