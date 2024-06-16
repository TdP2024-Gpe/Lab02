class Dictionary:
    def __init__(self, dict={}):
        self._dict = dict

    def loadDictionary(self, dict_phat):
        # dict is a string with the filename of the dictionary
        with open(dict_phat, "r") as f:

            for li in f:
                key_value = li.strip().split()
                if len(key_value) >= 2:
                    for i in range(1, len(key_value)):
                        if key_value[0] not in self._dict:
                            self._dict[f"{key_value[0]}"] = [f"{key_value[i]}"]
                        else:
                            self._dict[f"{key_value[0]}"].append(f"{key_value[i]}")
        # print(self._dict)

    def add_word(self, entry, path_file):
        key_value = entry.strip().split()
        if len(key_value) >= 2:
            for i in range(1, len(key_value)):
                if key_value[0] not in self._dict:
                    self._dict.update({f"{key_value[0]}": [f"{key_value[i]}"]})
                else:
                    self._dict[f"{key_value[0]}"].append(f"{key_value[i]}")
        self.writefile(path_file)

    def translate(self, query):
        if self._dict.get(query):
            return self._dict[query]
        else:
            return "\nLa parola cercata non è presente nel dizionario."

    def translateWordWildCard(self):
        pass

    def print_all(self):
        for x, y in self._dict.items():
            print(x, y)

    def writefile(self, path_file):
        _w = ""  # Stringa da scrivere nel file punti.txt
        _f = open(path_file, "w")

        for key, value in self._dict.items():
            if len(value) >= 2:
                _w = _w + (f"{key} ")
                for i in range(0, len(value)):
                    if i < len(value) - 1:
                        _w = _w + (f"{value[i]} ")
                    else:
                        _w = _w + (f"{value[i]}\n")
            else:
                _w = _w + (f"{key} {value[0]}\n")

        _f.write(f"{_w}")
        _f.close()
        # print(f"\nLa classifica attuale è:\n{_w}")
