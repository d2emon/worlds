from ..thing import Thing
from ..name_generators import NameGenerator, ThingName


UNIVERSE_DATA = [
    # Thing("multiverse",["universe,10-30"],[
    #   "multiverse","lasagnaverse","doughnutverse","towelverse","baconverse","sharkverse","nestedverse","tastyverse",
    #   "upverse","downverse","layerverse","clusterverse","metaverse","quantiverse","paraverse","epiverse",
    #   "alterverse","hypoverse","dimensioverse","planiverse","pluriverse","polyverse","maniverse","stackoverse",
    #   "antiverse","superverse","upperverse","maxiverse","megaverse","babyverse","tinyverse","retroverse",
    #   "ultraverse","topoverse","otherverse","bubbleverse","esreverse","versiverse","'verse","cookieverse",
    #   "grandmaverse"
    # ])
    Thing("universe", [["supercluster", (10, 30)]]),
    Thing("supercluster", [["galaxy", (10, 30)]], ThingName("galactic supercluster")),
    Thing("galaxy", [
        ["galaxy center"],
        ["galaxy arm", (2, 6)],
    ]),
    Thing("galaxy arm", [
        ["galactic life", None, 5],
        ["dyson sphere", None, 4],
        ["dyson sphere", None, 2],
        ["star system", (20, 50)],
        ["nebula", (0, 12)],
        ["black hole", None, 20],
        ["black hole", None, 20],
    ], ThingName("arm")),
    Thing("galaxy center", [
        ["black hole"],
        ["galactic life", None, 10],
        ["dyson sphere", None, 4],
        ["dyson sphere", None, 2],
        ["star system", (20, 50)],
        ["nebula", (0, 12)],
    ], ThingName("galactic center")),
    Thing("nebula", [
        ["galactic life", None, 15],
        ["star", None, 2],
        ["star", None, 2],
        ["star", None, 2],
        ["interstellar cloud", (1, 6)],
    ]),
    Thing("interstellar cloud", [
        ["helium"],
        ["hydrogen"],
        ["carbon", None, 80],
        ["water", None, 5],
        ["ammonia", None, 5],
        ["nitrogen", None, 5],
        ["iron", None, 5],
        ["sulfur", None, 5],
        ["oxygen", None, 15],
    ], NameGenerator(
        [
            "a bright pink", "a faint", "a fading", "a pale", "a fluo", "a glowing", "a green", "a bright green",
            "a dark brown", "a brooding", "a magenta", "a bright red", "a dark red", "a blueish", "a deep blue",
            "a turquoise", "a teal", "a golden", "a multicolored", "a silver", "a dramatic", "a luminous",
            "a colossal", "a purple", "a gold-trimmed", "an opaline", "a silvery", "a shimmering"
        ],
        [" "],
        ["interstellar cloud"],
    )),
    Thing("star system", [
        ["star"],
        ["star", None, 3],
        ["visitor planet", None, 5],
        ["future planet", None, 10],
        ["future planet", None, 10],
        ["terraformed planet", None, 50],
        ["terraformed planet", None, 20],
        ["terraformed planet", None, 10],
        ["medieval planet", None, 30],
        ["medieval planet", None, 20],
        ["ancient planet", None, 50],
        ["ancient planet", None, 30],
        ["ancient planet", None, 10],
        ["barren planet", None, 60],
        ["barren planet", None, 40],
        ["barren planet", None, 20],
        ["gas giant", None, 60],
        ["gas giant", None, 40],
        ["gas giant", None, 20],
        ["gas giant", None, 10],
        ["asteroid belt", (0, 2)],
    ]),
    Thing("dyson sphere", [
        ["star"],
        ["star", None, 3],
        ["dyson surface"],
        ["future planet", (1, 8)],
        ["barren planet", None, 60],
        ["barren planet", None, 40],
        ["barren planet", None, 20],
        ["gas giant", None, 60],
        ["gas giant", None, 40],
        ["gas giant", None, 20],
        ["gas giant", None, 10],
        ["asteroid belt", (0, 2)],
    ]),
    Thing("star", [
        ["ghost", None, 0.1],
        ["space monster", None, 0.2],
        ["hydrogen"],
        ["helium"],
    ], NameGenerator(
        [
            "white", "faint", "yellow", "red", "blue", "green", "purple", "bright", "double", "twin", "triple", "old",
            "young", "dying", "small", "giant", "large", "pale", "dark", "hell", "horrific", "twisted", "spectral"
        ],
        [" star"]
    )),
    # new Thing("planet",[".terraformed planet"],"telluric planet");
    Thing("barren planet", [
        ["galactic life", None, 10],
        ["rock"],
        ["ice", None, 50],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("visitor planet", [
        ["visitor city", (1, 8)],
        ["visitor installation", (2, 6)],
        ["galactic life"],
        ["rock"],
        ["ice", None, 50],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("future planet", [
        ["future continent", (2, 7)],
        ["ocean", (1, 7)],
        ["future sky"],
        ["future moon", None, 30],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("terraformed planet", [
        ["continent", (2, 7)],
        ["ocean", (1, 7)],
        ["terraformed sky"],
        ["terraformed moon", None, 30],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("medieval planet", [
        ["medieval continent", (2, 4)],
        ["ancient continent", (0, 3)],
        ["ocean", (1, 7)],
        ["sky"],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("ancient planet", [
        ["ancient continent", (2, 7)],
        ["ocean", (1, 7)],
        ["sky"],
        [".planet composition"],
    ], ThingName("telluric planet")),
    Thing("planet composition", [
        ["planet core"],
        ["moon", None, 40],
        ["moon", None, 20],
        ["moon", None, 10],
    ], ThingName("planet")),
    Thing("moon", [
        ["ghost", None, .1],
        ["rock"],
        ["planet core"],
    ], NameGenerator(
        ["young", "old", "large", "small", "pale", "white", "dark", "black", "old"],
        [" moon"],
    )),
    Thing("terraformed moon", [
        [".planet composition"],
        ["continent", (1, 4)],
        ["ocean", (1, 4)],
        ["sky"],
    ], NameGenerator(
        [
            "young", "old", "large", "small", "pale", "white", "dark", "black", "old", "green", "lush", "blue",
            "city", "colonized", "life",
        ],
        [" moon"],
    )),
    Thing("asteroid belt", [
        ["galactic life", None, 20],
        ["asteroid", (10, 30)],
    ]),
    # new Thing("earth",[".asteroid belt"],"Earth");
    Thing("asteroid", [
        ["space animal", None, .5],
        ["rock"],
        ["ice", None, 30],
    ]),
    Thing("gas giant", [
        ["gas giant atmosphere"],
        ["planet core", None, 50],
        ["moon", (0, 3)],
        ["terraformed moon", None, 20],
        ["terraformed moon", None, 10],
    ]),
    Thing("gas giant atmosphere", [
        ["galactic life", None, 10],
        ["helium"],
        ["hydrogen"],
        ["water", None, 50],
        ["ammonia", None, 50],
        ["methane", None, 50],
    ], ThingName("atmosphere")),
    Thing("planet core", [
        ["space monster", None, 0.5],
        ["iron"],
        ["rock"],
        ["diamond", None, 2],
        ["magma"],
    ], "core"),

    Thing("black hole", [["inside the black hole"]]),
    Thing("inside the black hole", [
        ["end of universe note", None, .5],
        ["crustacean", None, .2],
        ["white hole"],
    ]),
    Thing("white hole", [["universe"]]),
    # Thing("42",["universe"]),
    # Thing("everything",["universe"]),
    Thing("end of universe note", [
        ["pasta", None, .1],
    ], NameGenerator([
        "Help! I'm trapped in a universe factory!",
        "Okay, you can stop clicking now.",
        "I want to get off Mr Orteil's Wild Ride",
        "my sides",
    ])),
    # Thing("orteil",["body","orteil psyche","clothing set","computer"],"Orteil")
    # Thing("god",[".orteil"],"Orteil")
    # Thing("orteil psyche",["orteil thoughts"],"psyche")
    # Thing("orteil thoughts",[], [
    #   "OH MY GOD WHAT ARE YOU DOING HERE TURN BACK IMMEDIATELY","WHAT IS WRONG WITH YOU","WHAT THE HELL GO AWAY",
    #   "WHAT ARE YOU DOING OH GOD","WHY THE HELL ARE YOU HERE","I DO WHAT I WANT OKAY","NO I DON'T CARE GO AWAY",
    #   "WHAT DID I EVEN DO TO YOU","OH NO WHY THIS",
    #   "OKAY JUST <a href=\"http://orteil.deviantart.com\">GO THERE ALREADY</a>",
    #   "<a href=\"http://twitter.com/orteil42\">WHATEVER</a>"]);
]