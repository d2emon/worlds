from ..thing import Thing, ChildrenGenerator
from ..name_generators import NameGenerator, ThingName


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

    # Towns
    Thing("village", [
        ["residential area", (1, 4)],
        ["commercial area", None, 90],
        ["police station", None, 50],
        ["fire department", None, 40],
        ["museum", None, 5],
        ["library", None, 40],
        ["farm", (0, 6)],
        ["factory", (0, 2)],
        ["cemetery", None, 60],
        ["research facility", None, 4]
    ], ThingName("village")),
    Thing("city", [
        ["monument", None, 15],
        ["monument", None, 5],
        ["residential area", (4, 9)],
        ["commercial area", (1, 5)],
        ["police station"],
        ["police station", None, 50],
        ["fire department"],
        ["fire department", None, 50],
        ["museum", None, 40],
        ["library", None, 60],
        ["hospital"],
        ["farm", (0, 3)],
        ["factory", (1, 4)],
        ["cemetery"],
        ["research facility", None, 2],
    ], ThingName("city")),
    Thing("capital", [
        ["monument", None, 70],
        ["monument", None, 40],
        ["monument", None, 10],
        ["residential area", (7, 15)],
        ["commercial area", (3, 9)],
        ["police station", (2, 5)],
        ["fire department", (1, 3)],
        ["museum", (1, 2)],
        ["library", (1, 3)],
        ["hospital", (1, 3)],
        ["farm", (0, 2)],
        ["factory", (2, 6)],
        ["cemetery"],
        ["cemetery", None, 50],
        ["research facility", None, 1]
    ], ThingName("capital city")),
]
