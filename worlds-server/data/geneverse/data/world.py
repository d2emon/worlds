from ..thing import Thing, ChildrenGenerator
from ..name_generators import NameGenerator


WORLD_SUBDIVISIONS_DATA = [
    Thing("biome", [
        ["plain", (1, 5)],
        [
            ["forest", (0, 4)],
            ["jungle", (0, 4)],
        ],
        ["mountain", (0, 3)],
    ]),

    Thing("continent", [
        ["country", (1, 10)],
        ["sea", (1, 5)],
    ], NameGenerator(
        ["continent of "],
        ["A", "Eu", "Ame", "Ocea", "Anta", "Atla"],
        ["frica", "rtica", "ropa", "rica", "nia", "sia", "ntide"],
    )),
    # (
    #   ["Eu","A","O","E"],
    #   ["rt","lt","rm","t","tr","tl","str","s","m","fr"],
    #   ["a","o","e","i"],
    #   ["ri","ni","ti","fri","",""],
    #   ["sia","nia","ca"],
    # )
    Thing("country", [
        ["region", (1, 10)],
        ["battlefield", None, 10],
        [".biome"],
    ], NameGenerator(
        ["country of "],
        [
            "Li", "Arme", "Le", "Molda", "Slove", "Tur", "Afgha", "Alba", "Alge", "Tu", "Fran", "Baha", "Su", "Austra",
            "Germa", "In", "Ara", "Austri", "Be", "Ba", "Bra", "Ru", "Chi", "Ja", "Tai", "Bangla", "Gha", "Bou", "Bo",
            "Tas", "Ze", "Mon", "Mo", "Ne", "Neder", "Spai", "Portu", "Po", "Por", "Mol", "Bul", "Bru", "Bur", "Gro",
            "Syl", "Gui", "Da", "Gree", "Bri", "Ita"
        ], [
            "ly", "dania", "mas", "vania", "ce", "nea", "nau", "topia", "garia", "gal", "laska", "golia", "nisia",
            "land", "snia", "livia", "mania", "than", "nin", "pan", "wan", "zil", "ssia", "na", "rein", "lgium", "bia",
            "ny", "ce", "stan", "distan", "nistan", "dan", "lia", "nia", "via", "sia", "tia", "key", "desh", "dia"
        ],
    )),
    Thing("region", [
        ["capital"],
        ["city", (1, 10)],
        ["village", (2, 15)],
    ], NameGenerator(
        [
            "north ", "east ", "south ", "west ", "north-west ", "north-east ", "south-west ", "south-east ",
            "center ", "oversea "
        ],
        ["hilly", "rainy", "lush", "foggy", "desertic", "green", "tropical", "rich", "barren", "scorched"],
        [" region"]
    )),
]
