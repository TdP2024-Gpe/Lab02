import dictionary as dc

d = dc.Dictionary()


class Translator:

    def __init__(self):
        pass

    def handle_add(self, entry, path_file):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        d.add_word(entry, path_file)
        return "Parola aggiunta!"

    def handle_translate(self, query):
        # query is a string <parola_aliena>
        return d.translate(query)

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        pass
