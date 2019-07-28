from .age import Age, Date


def FA(*date):
    return Date('gondor-age', *date)


def SA(*date):
    return Date('gondor-age', *date)


def TA(*date):
    return Date('gondor-age', *date)


# def FA(*date):
#     return Date(Age.find('fourth-age'), *date)


class Event:
    def __init__(
        self,
        date,
        desc,
    ):
        self.date = date
        self.desc = desc


"""
Третья Эпоха — эпоха в истории Средиземья длившаяся 3019 лет. Во время этой 
Эпохи на эльфах в большей мере стало сказываться угасание, вследствие чего они 
активно покидали Средиземье. Лишь три поселения эльфов, два из которых 
оберегались от угасания Тремя Кольцами, продолжали существовать в Средиземье 
до конца Эпохи. Семь Колец гномов, пробуждали в них алчное желание добывать 
больше сокровищ, что привело к падению многих гномьих королевств из-за атак 
драконов; величайшее из них, Мориа, пало вследствие пробуждения в глубинах 
Балрога. Культура немногочисленных нуменорцев в Средиземье постепенно 
утрачивалась, а народ их смешивался с прочими племенами людей.

Когда Саурон начал вновь набирать мощь, в Средиземье появляются Истари, 
посланные Валар для помощи народам Средиземья одолеть Саурона.

Более прочего, данная Эпоха характеризуется полной победой над Сауроном в ходе 
Войны Кольца (вследствие уничтожения Кольца Всевластия).

Третья Эпоха завершилась 29 сентября 3021 года. В этот день хранители Кольца 
Всевластья (Бильбо и Фродо) и Трёх Эльфийских колец (Гэндальф, Элронд и 
Галадриэль) отплыли из Серой Гавани в Валинор.

— 3021 years long Note on Shire Reckoning: Year 1601 of the Third Age, in 
which the Shire was founded, is year 1 of the Shire Reckoning. Thus, Third Age 
years can be converted into their Shire equivalents by deducting 1600.

"""

EVENTS = [
    # Третья эпоха
    # I
    Event(
        date=TA(1),
        desc="""Исильдур, сын Элендиля Высокого, провозглашает свою власть над 
        Дунаданами Севера и Юга. Он остается в Гондоре, восстанавливая порядок 
        в королевстве, отправляя большую часть армии Арнора в Эриадор""",
    ),
    Event(
        date=TA(2),
        desc="""Исильдур сажает в Минас Аноре семя Белого Древа. Он поручает 
        правление Южным Королевством Менелдилю. Исильдур и трое его старших 
        сыновей погибают в Оболони.
        
        Planting of the Second White Tree at Minas Tirith, Death of Isildur by 
        orcs in the Battle of the Gladden Fields, loss of the One Ring in the 
        Gladden river.
        
        Исильдур сажает Белое Древо в Минас Анор. Он отправляется в Ималдрис в 
        начале Иваннета (сентябрь) и после присоединения южного королевства 
        поручает правление Южным Королевством Менелдилю. Однако на тридцатый 
        день своего путешествия у северных границ Гладденских полей Исильдур и 
        его три старших сына, Элендур, Аратан и Сирион, были убиты в Оболони 
        напавшими урками. Единое Кольцо потеряно в Андуине""",
    ),
    Event(
        date=TA(3),
        desc="""Охтар приносит обломки Нарсиля в Имладрис.
        
        Ohtar brings the rests of Narsil to Rivendell.
        
        Охтар, которому Исильдур передал обломки Нарсиля, достигает Ималдриса 
        после того, как избежал атаки урков на Гладденских полях.""",
    ),
    Event(
        date=TA(10),
        desc="""Валандиль становится королем Арнора.
        
        Valandil becomes king of Arnor.
        
        Валандиль становится королем Арнора.""",
    ),
    # II
    # III
    # IV
    # V
    # VI
    # VII
    # VIII
    # IX
    # X
    # XI
    # XII
    # XIII
    # XIV
    # XV
    # XVI
    # XVII
    # XVIII
    # XIX
    # XX
    # XXI
    # XXII
    # XXIII
    # XXIV
    # XXV
    # XXVI
    # XXVII
    # XXVIII
    # XXIX
    # XXX
    # XXXI
]

# I
"""
"""
# II
"""
109 — Элронд берет в жены Келебриан, дочь Келеборна.
130 — Рождение сыновей Элронда — Элладана и Элрохира.

TA 109 - Elrond weds Celebrían, daughter of Celeborn and Galadriel.
TA 130 - Elrohir and Elladan are born to Elrond and Celebrían.
"""
# III
"""
241 — Рождение Арвен.

TA 241 - Arwen Undómiel is born to Elrond and Celebrían.
"""
# V
"""
420 — Король Остохэр отстраивает Минас Анор.
480 — Рождение Атанатара I.
490 — Первое вторжение Вастаков.
500 — Ромендакиль I наносит поражение вастакам.

TA 420 - King Ostoher rebuilds Minas Anor.
TA 490 - Easterlings invade Gondor.
TA 500 - Easterlings defeated by King Rómendacil I.
"""
# VI
"""
541 — Гибель Ромендакиля.
570 — Рождение Сириондиля.

TA 541 - Easterlings invade Gondor once more, slaying King Rómendacil.
c. TA 550 - King Turambar of Gondor defeats the Easterlings of Rhûn; the Kingdom of Rhovanion becomes an ally of Gondor.
"""
# VII
"""
667 — Смерть Турамбара. Атанатар I вступает на трон Гондора.
"""
# VIII
"""
748 — Смерть Атанатара I. Сириондиль вступает на трон Гондора.
"""
# IX
"""
830 — Смерть Сириондиля. Фаластур начинает род «Морских Королей» Гондора.
861 — Смерть Эарендура и раздел Арнора.

TA 830- King Siriondil of Gondor passes. His elder son Tarannon Falastur begins the line of Ship-kings
TA 861 - Following Eärendur's death, the Kingdom of Arnor breaks up into Arthedain, Cardolan and Rhudaur.
"""
# X
"""
933 — Эарниль I берет Умбар и превращает его в крепость Гондора.
936 — Эарниль пропадает в Море.
1000 — Саурон появляется в южном Лихолесье. Отступление нандор на север.

TA 933 - Eärnil I of Gondor takes Umbar in a surprise attack.
TA 936 - Eärnil I lost at sea.
TA 1000 - The Istari come to Middle-earth.
"""
# XI
"""
1015 — Кириандиль сражен при осаде Умбара
1050 — Хьярмендакиль I покоряет Харад. Гондор достигает вершины могущества. Тень покрывает Ясный Бор, и он получает название Сумеречья. В летописных сводах впервые упоминается название Перианы, в Эриадор приходят Мохноноги.

TA 1015 - King Ciryandil slain in siege of Umbar; Hyarmendacil I ascends throne of Gondor.
TA 1015 - Black Númenóreans of Umbar besiege their old city.
TA 1030 - Siege of Umbar ends, Umbar retaken by Black Númenóreans.
TA 1050 - Hyarmendacil I, king of Gondor, conquers Harad; Sauron appears in southern Greenwood, which is soon renamed Mirkwood; Hobbits begin to migrate into Eriador.
"""
# XII
"""
1140 — Истари узнают о поселении в Дол Гулдуре злой силы и решают, что это один из назгул.
1149 — Начало правления Атанатара Алькарина
1150 — В Эриадоре появляются Лесовики. Хваты проходят Перевал Красного Рога и расселяются у Седонны и в Дунгарских землях.

TA 1149 - Death of Hyarmendacil I, Atanatar takes the sceptre of Gondor.
"""
# XIII
"""
1300 — Вновь появляются лиходейские твари. В Мглистых Горах множатся орки и нападают на гномов. Снова появляются назгул, их предводитель приходит в Ангмар. Перианы идут дальше на запад, многие оседают в Брыле.

c. TA 1200 - Rulers of Rhovanion assume the title "King of Rhovanion".
TA 1225 - Legolas born
TA 1248 - Rómendacil II of Gondor strikes decisive blow to the Easterlings; forms a strong alliance with Rhovanion, to which he cedes all the lands east of Anduin.
TA 1255 - Eldacar born.
TA 1259 - Castamir born.
TA 1300 - The Witch-king travels north and assumes control of Angmar.
"""
# XIV
"""
1356 — Аргелеб I гибнет в битве с Рудауром. Примерно в это же время Хваты покидают Седонну, и некоторые возвращаются в Ровенион.

TA 1344 - The death of Vidumavi.
TA 1356 - King Argeleb I of Arthedain is killed during an invasion by Rhudaur, now controlled by Angmar; his son, Arveleg I, ascends the throne.
TA 1366 - Valacar ascends the throne of Gondor.
"""
# XV
"""
1409 — Король-Чародей вторгается в Арнор. Гибель Арвелега I. Форност и Тирн Гортад защищаются. Крепость на Амон Сул разрушена.
1432 — В Гондоре умирает король Валакар, и начинается междоусобица.
1437 — Сожжен Осгилиат. Палантир утрачен. Эльдакар бежит в Рованион. Смерть Орнендиля.
1447 — Эльдакар возвращается и изгоняет узурпатора Кастамира. Битва у бродов Эруи. Осада Пеларгира.
1448 — Мятежники бегут и захватывают Умбар.

TA 1409 - Cardolan is conquered by the kingdom of Angmar and Rhudaur disappears; Weathertop watchtower, and fortifications are burned and destroyed. Annuminas  is attacked, sacked and abandoned in ruins until the Fourth Age.
TA 1432 - Eldacar succeeds his father, Valacar, as king of Gondor.
TA 1437 - Castamir the Usurper, Lord of Ships, usurps throne of Gondor (see Kin-strife); Osgiliath's Palantír is lost in the river.
TA 1447 - Eldacar reclaims Gondor with a Rhovanion army and kills Castamir.
TA 1448 - Sons of Castamir the Usurper and most of the fleet of Gondor flee south to Umbar; they become known as the Corsairs of Umbar.
TA 1490 - Death of Eldacar; his son Aldamir becomes king.
"""
# XVI
"""
1540 — Король Альдамир гибнет в войне с Харадом и умбарскими пиратами.
1551 — Хьярмендакиль II побеждает харадрим.

TA 1540 - King Aldamir of Gondor is slain by Haradrim.
TA 1551- King Hyarmendacil II annihilates the Haradrim in battle and avenges his father's death eleven years prior.
TA 1600 - Two Fallohide (see Hobbit) brothers decided to cross the River Baranduin and settle on the other side, and are followed by large numbers of Hobbits.
"""
# XVII
"""
1601 — Многие перианы уходят из Пригорья, и король Аргелеб II дарует им земли за Берендуином.
1630 — Из Дунгара к перианам переселяются Хваты.
1634 — Пираты разоряют Пелагир и убивают короля Минардиля.
1636 — Великая Чума опустошает Гондор. Смерть короля Телемнара и его детей. В Минас Аноре засыхает Белое Древо. Чума захватывает северные и запдные области, население их вымирает. Перианы за Берендуином выживают, но терпят большие потери.
1640 — Король Тарондор переносит королевский дворец в Минас Анор и сажает семя Белого Дерева. Осгилиат превращается в руины. Мордор остаётся без охраны.

TA 1601 - The Shire is first settled by Hobbits.
TA 1634 - The Corsairs of Umbar attack Gondor, slaying king Minardil at Pelargir, and raiding the city.
TA 1636 - The Great Plague decimates Gondor and Rhovanion; the watch on Mordor fails.
TA 1640 - The capital of Gondor is moved from Osgiliath to Minas Anor.
"""
# XIX
"""
1810 — Король Телумехтар Умбардакил отвоевывает Умбар и изгоняет пиратов.
1851 — Первые нападения кочевников на Гондор.
1856 — Восточные владения Гондора захвачены врагами. В битве на Равнинах погибает король Нармакиль II.
1899 — Король Калимехтар наносит кочевникам поражение в битве при Дагорладе.
1900 — Калимехтар возводит в Минас Аноре Белую башню.

TA 1810 - King Telumehtar of Gondor conquers Umbar; renames himself Umbardacil.
TA 1851 - Wainriders overrun the Kingdom of Rhovanion and begin attacking Gondor.
TA 1856 - Eastern territories of Gondor lost; King Narmacil II slain in battle.
TA 1899 - Gondor attacks Wainriders from the east; the Kingdom of Rhovanion, occupied by Wainriders, rebels and is freed.
TA 1900 - White Tower constructed in Minas Anor.
"""
# XX
"""
1940 — Заключен союз Арнора и Гондора. Арведуи женится на Фириэль, дочери Ондохера.
1944 — Ондохер и его наследники погибают в битве. Эарниль выбивает харадрим из Южного Итилиена. Битва в Лагере. Арведуи требует корону Гондора.
1945 — На престол Гондора вступает Эарниль II.
1974 — Конец Северного Королевства. Король-Чародей опустошает Артедайн и захватывает Форност.
1975 — Арведуи тонет в Форохельском заливе. Палантиры Аннуминоса и Амон-Сула утрачены. Эарнур приводит флот в Линдон. Король-Чародй разбит в битве при Форносте.
1976 — Аранарт становится вождем дунэдайн. Знаки власти королей передаются на хранение Элронду.
1977 — Фрумгар уводит Эотеод на север.
1979 — Скокка из Марей становится первым Таном Шира.
1980 — Король-Чародей приходит в Мордор и собирает там назгул. В Мории появляется Балрог и убивает Дарина VI.
1981 — Балрог убивает Наина I. Гномы покидают Морию. Лесные эльфы Лориена уходят на юг. Нимродэль теряется. Гибель Амрота.
1999 -Траин I приходит в Эребор и основывает Королевство-под-Горой (Подгорное королевство).
2000 — Назгул выходят из Мордора и осаждают Минас-Итиль.

TA 1936 - Ondoher succeeds Calimehtar as king of Gondor.
TA 1944 - During an invasion by the Wainriders and the Haradrim, King Ondoher of Gondor is slain in battle with his sons; the Gondorian general Earnil defeats their Haradrim allies at the Battle of South Ithilien and then defeats the Wainriders at the Battle of the Camp; Arvedui, son-in-law of Odonher claims the crown of Gondor; Haradrim, Wainriders and the Variags of Khand take Umbar; new Corsairs of Umbar emerge.
TA 1945 - Pelendur, steward to Ondoher, rejects Arvedui's claim and the crown is instead given to the victorious general Earnil.
TA 1964 - Arvedui, son of King Araphant of Arthedain, ascends the throne.
TA 1974 - The kingdom of Arthedain is conquered by Angmar. Fornost is destroyed and left in ruins until the Fourth Age.
TA 1975 - Armies of Gondor and Lindon destroy Angmar in the Battle of Fornost; death of Arvedui.
TA 1980 - The Moria dwarves awaken Durin's Bane, a Balrog, which kills Durin VI, king of Khazad-dûm; the Nazgûl return to Mordor.
TA 1981 - Durin VI's son, Náin, is also killed, and the dwarves flee Moria; deaths of Amroth and Nimrodel
TA 1999 - The Dwarvish Kingdom of the Lonely Mountain (Erebor) is founded. About this time Vorondil the Hunter, son of Pelendur, hunts the Kine of Araw in the fields of Rhun.
TA 2000 - The Nazgûl attack Minas Ithil, capturing it (and the palantír kept there) after a two-year siege.
"""
# XXI
"""
2002 — Захват Минас-Итиля и превращение его в Минас-Моргул. Палантир захвачен.
2043 — Королем Гондора становится Эарнур. Король-Чародей вызывает его на поединок.
2050 — Повторный вызов. Эарнур скачет к Минас-Моргулу и исчезает. Мардиль становится первым намесником-правителем.
2060 — Мощь Дол-Гулдура растет. Мудрые начинают подозревать в хозяине Дол-Гулдура возродившегося Саурона.
2063 — В Дол-Гулдур приходит Гэндальф. Саурон отсупает и скрывается на востоке. Начинается Бдительный Мир. Назгул остаются в Минас-Моргуле, но не предпринимают каких-либо действий.

TA 2050 - End of the royal dynasty of Gondor (until the return of King Elessar).
TA 2060 - As the power of Dol Guldur grows, the Wise suspect it is Sauron taking shape again.
TA 2063 - Gandalf travels to Dol Guldur; Sauron flees into the East, beginning the Watchful Peace.
"""
# XXIII
"""
2210 — Торин I уходит из Эребора в Серые горы. Там собирается большая часть народа Дарина.
"""
# XXIV
"""
2340 — Изумбрас I становиться Тринадцатым Таном и первым Таном из рода Туков. Староскоки занимают Заскочье.
"""
# XXV
"""
2460 — Бдительный Мир заканчивается. Саурон возвращается в Дол-Гулдур.
2463 — Собирается Первый Белый Совет. Примерно в это же время хват Деагорл находит Кольцо Всевластья. Смеагорл душит его.
2470 — Смеагорл-Голлум укрывается в Мглистых Горах.
2475 — Нападения на Гондор возобновляются. Осгилиат окончательно разрушен. Его мост лежит в руинах.
около * 2480 — Орки строят тайные укрепления в Мглистых горах и укрепляют привалы, ведущие в Эриадор. Саурон населяет Морию своими тварями.

TA 2430 - The approximate birth year of Sméagol.
TA 2460 - Sauron returns with increased strength to Dol Guldur, ending the Watchful Peace.
TA 2463 - The White Council is formed; Sméagol (later known as Gollum) becomes the fourth master of the One Ring, after killing his cousin Déagol.
"""
# XXVI
"""
2509 — Келебриан попадает в засаду на пути в Лориен у Перевала красного Рога на Карадрасе. Она ранена отравленной стрелой.
2510 — Келебриан уходит за Море. Орки разоряют Каленардон. Эорл Юный одерживает победу на полях Келебранта. Роххиримы заселяют Каленардон.
2545 — Гибель Эорла.
2569 — Брего, сын Эорла достраивает Золотой Дворец.
2570 — Балдор, сын Брего, входит в Запретную Дверь и исчезает. Примерно в это же время на дальнем севере вновь появляются драконы и начинают беспокоить гномов.
2589 — Война гномов и драконов. Смерть Даина I
2590 — Трор возвращается в Эребор. Его брат, Грор, уходит в Рудный Кряж.

TA 2509 - Cirion, Steward of Gondor, sends summons to the Éothéod for military aid; Celebrían is waylaid by orcs, receives a poisoned wound, and consequently departs Middle-earth for Valinor.
TA 2510 - The alliance between Rohan and Gondor comes into existence. The Easterlings launch a massive invasion of Gondor. The Balchoth invade Rhovanion (which disappears as an independent realm) and Gondor, conquering much of Calenardhon, but are driven back by the people of Éothéod; Gondor gives the now-uninhabited province of Calenardhon to the people of Éothéod.
TA 2545 - Eorl the Young, 1st king of Rohan, dies in the battle in the Wold against the Easterlings. Brego succeeds him as the 2nd King of Rohan.
TA 2569 - Construction of the Golden Hall in Rohan.
TA 2570 - Aldor, aged only 26, becomes 3rd king of Rohan at the death of his father Brego; dragons reappear in the far north, coming into conflict with the dwarves.
"""
# XXVII
"""
2644 — Рождение Траина II и Деора
2670 — Тобольд сажает в Южной Чети «трубочное зелье»
2683 — Изенгрим II становится Таном и начинает рыть Смеалища
2698 — Эктелион I восстанавливает в Минас-Тирите Белую Башню.

2645 - Fréa becomes 4th king of Rohan after the death of his father Aldor ('the Old')
TA 2659 - Fréawine, 5th King of Rohan.
TA 2680 - Goldwine, 6th King of Rohan.
TA 2699 - Déor, 7th King of Rohan.
"""
# XXVIII
"""
2740 — Орки снова вторгаются в Эриадор.
2747 — Битва на Зелёных Полях.
2752 — Рождение Белектора II.
2758 — Рохан подвергается нападению и разорению. Флот пиратов атакует Гондор. Хельм Роханский укрывается в Хельмовой Пади. Вулф захватывает Эдорас. Следует Долгая Зима. В Эриадоре и Рохане много жертв. Гэндальф приходит на помощь хоббитам.
2759 — Смерть Хельма. Фреалаф изгоняет Вулфа, с него начинается вторая ветвь роханских королей. Саруман поселяется в Изенгарде.
2770 — Смауг нападает на Эребор. Эсгарот разрушен. Трор с Трайном II и Торином II спасаются.
2790 — Трор гибнет в Мории. Гномы собирают войска для мести. В Шире родился Геронтиус, прозванный позже Старым Туком.
2793 — Война орков и гномов.
2799 — Битва в Нандухирионе перед Вратами Мории. Даин Железностоп возвращается в Рудный Кряж. Трайн II с Торином уходят на Запад и поселяются на юге Эред Луина, за Широм (2802)

TA 2718 - Gram, 8th King of Rohan.
TA 2741 - Helm Hammerhand 9th King of Rohan ascends the throne as last king of the first line.
TA 2746 - Arminas,15th Prince of Dol Amroth, falls while defending Tol-en-Antered against the Corsairs of Umbar. Thorin Oakenshield is born.
TA 2758 - Dunlendings, under Wulf, invade Rohan, supported by the Corsairs of Umbar.
The Long Winter of Eriador; the Dunlendings lay siege to Hornburg.
TA 2759 - Helm Hammerhand, king of Rohan, is killed by the Dunlendings. He is succeeded by his nephew Fréaláf Hildeson; Saruman settles in Isengard.
TA 2763 - Balin is born.
TA 2767 - Dain II Ironfoot is born.
TA 2770 - Smaug lays waste to the town of Dale and captures Erebor with all of its treasure. The surviving dwarves there are driven into exile.
TA 2783 - Glóin is born.
TA 2790 - Thrór is murdered by Azog in Moria. The dwarves from all over Middle-earth begin their preparations for war.
TA 2793 - The War of the Dwarves and Orcs begins.
TA 2798 - Fréaláf Hildeson, tenth king of Rohan, dies. He is followed by his son Brytta Léofa.
TA 2799 - The Battle of Azanulbizar is fought on Moria's East Gate, in which the dwarves defeat the orcs and slay Azog but do not reoccupy Moria for fear of Durin's Bane.
"""
# XXIX
"""
2800-* 2864 — Бесконечные нападения орков на Рохан. Гибель короля Валды.
2841 — Трайн II уходит в Эребор. Его выслеживают шпионы Саурона.
2845 — Трайн заточен в Дол-Гулдуре. У него отбирают последнее из Семи Колец.
2850 — Гэндальф второй раз приходит в Дол-Гулдур и узнает в его хозяине Саурона. Гэндальф понимает, что Саурон собирает Кольца и ищет Кольцо Всевластья, в связи с чем разыскивает наследников Исильдура. Маг находит Трайна и получает Ключ Эребора. Трайн умирает в Дол-Гулдуре.
2851 — Собирается Белый Совет. Гэндальф советует атаковать Дол-Гулдур, но Саруман уговаривает Совет повременить, а тем временем сам начинает поиски Кольца в Оболони.
2852 — Белектор II Гондорский умирает. Засыхает Белое Древо.
2854 — Родились Эрлинг Гринхэнд — сын Холмана Гринхэнда и Хьюго Боффин — сын Отто Боффина и Лавандер Граб.
2855 — По наущению Саурона харадрим переходят Порос и вторгаются в Гондор. Сыновья Фолквайна Роханского погибают в боях за Гондор.
2890 — Рождение Бильбо.
2894 — Родился Джаго Боффин — старший сын Хьюго Боффина  и Доннамиры.

TA 2842 - Brytta Léofa, 11th king of Rohan, dies. Succeeded by his son Walda.
TA 2845 - Thráin II is captured by Sauron and imprisoned in Dol Guldur.
TA 2850 - Gandalf reenters Dol Guldur in secret and confirms that its master is indeed Sauron returned
TA 2851 - Gandalf urges the White Council to attack Dol Guldur, but is overruled by Saruman (who seeks the One Ring for himself); Walda, 12th King of Rohan, is killed by an orc, his son Folca succeeds him.
TA 2864 - Folca, 13th King of Rohan, is killed by the Boar of Everholt. He is succeeded by his son Folcwine.
TA 2879 - Gimli, son of Glóin, is born.
TA 2885 - Harondor is once again claimed by the Haradrim, supported by the Corsairs of Umbar. Fastred and Folcred, the twin sons of king Folcwine, are killed during the Battle of the Crossings of Poros.
22 September TA 2890 - Bilbo Baggins is born.
"""
# XXX
"""
2901 — Жители покидают Итилиен, спасаясь от набегов мордорских уруков. Строится убежище возле Хеннет Аннуна.
2907 — Родилась Гилраэнь, мать Арагорна II.
2911 — Лютая Зима. С севера в Эриадор приходят Белые Волки. Берендуин и прочие реки замерзли.
2912 — Великий разлив опустошает низовья Седонны и Берендуина. Опустошен Тарбад.
2918 — Родилась Лобелия Саквилль-Бэггинс.
2920 — Смерть Старого Тука.
2929 — Арахорн, сын Арадора берет в жены Гилраэнь.
2930 — Арадор убит троллями.
2931 — 1 марта рождается Арагорн, сын Арахорна II.
2933 — Арахорн II гибнет. Гилраэнь приносит Арагорна в Имладрис. Элронд принимает его, как сына и дает ему имя Эстель (Надежда), он тут же советует не раскрывать происхождение Арагорна. Родился Паладин Тук II.
2935 — В Минас-Тирите рождается Денетор II, сын Эктелиона II.
2937 — родился Виго Боффин, сын Джаго Боффина.
2938 — Родилась Росамунда Тук — мать Фредегара Болджера и Эстеллы Болджер, жены Мериадока Брендибака.
2939 — Саруману становится известно, что слуги Врага рыщут возле Оболони. Он понимает, что Саурону известно о гибели Исильдура, но скрывает свои мысли от Совета.
2940 — Родился Сарадок Брендибак. Родился Галмод — будущий отец Гримы Червеуста.
2941 — Торин Дубощит встречается с Гэндальфом. Они приходят к Бильбо. Поход. Бильбо встречается с Голлумом и становится владельцем Кольца Всевластья. Собирается Белый Совет. Саруман соглашается с планом нападения на Дол-Гулдур, стремясь помешать Саурону в поисках. Саурон отступает. В Битве Пяти Воинств гибнет Торин II Дубощит. Бард из Эсгарота убивает Смауга. Даин с Рудного Кряжа становится Королём-под-Горой.
2942 — Бильбо возвращается из похода с Кольцом. Саурон тайно возвращается в Мордор.
2944 — Бард отстраивает Эсгарот и становится Королем. Голлум вылезает на поверхность и начинает искать Бильбо.
2945 — Умер Хьюго Боффин.
2948 — У Тенгеля рождается сын Теоден.
2949 — Гэндальф и Балин навещают Бильбо в Шире.
2950 — Родилась Финдуилас, дочь Адрахила из Дол-Амрота.
2951 — Саурон открыто заявляет о себе и начинает собирать силы в Мордоре. Он восстанавливает Барад-Дур. Трое назгул занимают Дол-Гулдур. Голлум поворачивает к Мордору. Элронд открывает Арагорну его настоящее имя и происхождение, вручает обломки Нарсиля. Арвен возвращается из Лориэна и встречается с Арагорном. Арагорн уходит в Пустоземье.
2953 — В последний раз собирается Белый Совет. На нём спорят о Кольце. Саруман лжет, уверяя, что Кольцо сгинуло в Море. Саруман укрепляет Изенгард, устанавливая слежку за Гэндальфом, и отмечает его интерес к Ширу. Вскоре в Бри и Южной Чети появляются его шпионы.
2954 — Ородруин снова извергается. Последние жители Итилиена бегут за Андуин.
2956 — Арагорн встречается с Гэндальфом и они становятся друзьями.
2965 — Родился Хэмсон Гэмджи — брат Сэма Гэмджи.
2967-* 2980 — Продолжительные походы Арагорна. Он инкогнито служит правителям Рохана и Гондора.
2968 — Родился Фродо.
2969 — Родился Халфрид Гэмджи — брат Сэма Гэмджи.
2972 — Родилась Дэйзи Гэмджи — сестра Сэма Гэмджи.
2974 — Родился Грима Червеуст.
2975 — Родилась Перл Тук.
2976 — Денетор берет в жены Финдуилас из Дол-Амрота.
2977 — Бэйн, сын Барда, становится Королем Эсгарота.
2978 — Родился Боромир.
2979 — Родилась Пимпернель Тук.
2980 — Арагорн приходит в Лориен и снова встречается с Арвен. Он отдает ей Кольцо Барахира, и они обмениваются клятвами верности. Горлум достигает рубежей Мордора и знакомится с Шелоб. Теоден становится Королем Рохана.
2983 — Родился Фарамир, родился Сэмиус.
2984 — Смерть Эктелиона II. Денетор II становится наместником Гондора.
2986 — Умер Джаго Боффин.
2988 — Смерть Финдуилас.
2989 — Балин уходит в Морию.
2990 — Родился Перегрин Тук. Родился Эрхирион.
2991 — Родился Эомер, сын Эомунда.
2994 — Балин погибает. Попытка вернуть Морию провалилась.
2995 — Родилась Эовин, сестра Эомера.
3000 — Мощь Мордора растет. Саруман решает воспользоваться Палантиром Ортанка и выведать планы Врага, но попадает в ловушки Саурона, владеющего Камнем из Минас-Итиля. Саруман становится предателем. Ему доносят, что рубежи Шира охраняются Следопытами.

TA 2903 - Folcwine, 14th king of Rohan, dies and is succeeded by his youngest son Fengel.
TA 2907 - The birth of Gilraen (later wife of Arathorn II).
Fell Winter of TA 2911-TA 2912 - wolves invade the Shire. Tharbad is ruined in the following floods.
TA 2930 - Arathorn II becomes the Chieftain of the Dúnedain. Denethor II is born.
TA 2931 - Birth of Aragorn, called Estel until his coming of age, son of Arathorn II and Gilraen.
TA 2933 - Arathorn II is shot in the eye and killed while hunting orcs.
April 27, TA 2941 - Bilbo Baggins leaves Bag-end with Thorin II Oakenshield and company.
Midsummer's Eve (1 Lithe), TA 2941 - Elrond examines Thorin's map.
July 17, TA 2941 - Bilbo obtains the One Ring from Gollum.
July, TA 2941 - The White Council attacks Dol Guldur, which is abandoned by Sauron.
October, TA 2941 - Esgaroth is attacked by the dragon Smaug, who is consequentially killed by Bard the Bowman; Battle of the Five Armies. Thorin II Oakenshield dies and Dain II Ironfoot is crowned King under the Mountain.
TA 2942 - Bilbo returns to the Shire with the Ring. Sauron returns in secret to Mordor.
TA 2944 - Bard rebuilds Dale and becomes king. Gollum leaves the Mountains and begins to look for the "thief" of the Ring.
TA 2948 - Théoden, son of Thengel, king of Rohan, is born.
TA 2949 - Gandalf and Balin visit Bilbo in the Shire.
TA 2950 - Finduilas, daughter of Adrahil of Dol Amroth, is born.
TA 2951 - Sauron declares his presence in Mordor openly. Estel, later known as Aragorn, comes of age and is told about his heritage; the Corsairs of Umbar officially ally themselves with Mordor and destroy the great monument commemorating Ar-Pharazôn's victory over Sauron.
TA 2953 - The last meeting of the White Council.
Fengel, 15th King of Rohan, dies. His son Thengel returns to Rohan to succeed him.
TA 2956 - Aragorn first meets Gandalf the Grey.
TA 2957-TA 2980 - Aragorn as Thorongil serves in the armies of King Thengel of Rohan, and Steward Ecthelion II of Gondor.
September 22, TA 2968 - Frodo Baggins is born.
TA 2976 - Denethor II marries with Finduilas.
TA 2977 - Bain, son of Bard, become King of Dale.
TA 2978 - Boromir, son of Denethor II, is born.
TA 2980 - Arwen pledges her hand in marriage to Aragorn; Frodo Baggins loses both of his parents in a boating accident; Aragorn, in the service of the Steward of Gondor Ecthelion II leads a taskforce south and kills the Captain of the Haven, ruler of Umbar; Sam Gamgee born4; Théoden, son of Thengel, becomes 17th king of Rohan after the death of his father. Théoden is the last king of the second line and also he is Prince of the Eotheod Reborn.
TA 2982 - The birth of Meriadoc Brandybuck (Merry).
TA 2983 - The birth of Faramir.
TA 2987 - The birth of Elphir, son of Prince Imrahil
TA 2989 - Frodo Baggins comes under the guardianship of Bilbo Baggins; a company of dwarves, led by Balin, try to recolonize Moria.
TA 2990 - The birth of Peregrin Took (Pippin).
TA 2991 - The birth of Éomer.
TA 2994 - Balin is killed; the dwarf-colony in Moria is destroyed.
TA 2995 - The birth of Éowyn.
"""
# XXXI
"""
3002 — Бильбо приходит в Дольн.
3004 — Гэндальф навещает Фродо в Шире.
3007 — Бранд, сын Бэйна становится Королем Эсгарота. Умирает Гилраэнь.
3008 — Осенью Гэндальф в последний раз навещает Фродо.
3009 — Голлум попадает в руки Саурона. Арвен возвращается в Имладрис.
3015 — Предполагаемая смерть Галмода, отца Гримы. Паладин Тук II становится Таном Шира. Умерли Ферумбрас Тук III и Амелия Саквиль-Бэггинс.
3017 — Голлум уходит из Мордора и попадает в руки Арагорна. Гэндальф отправляется в Минас-Тирит и читает Свиток Исильдура.

TA 3001 - Bilbo Baggins turns 111 and leaves the Shire. Gandalf enlists Aragorn's help in tracking Gollum, then finds Isildur's scroll in Minas Tirith describing the One Ring.
TA 3002 - Lalia Clayhanger, the matriarch of the Took clan, dies, aged 119, and possibly pushed by Pearl Took5; Bilbo settles in Rivendell.
TA 3009 - Aragorn captures Gollum at Gandalf's request, and brings him as a captive to King Thranduil's halls in Mirkwood.
TA 3014 - Saruman begins using his influence to weaken Théoden, 17th king of Rohan.
"""

"""
Далее события становятся очень важными и с этого времени проводится более подробная хронология великих лет.

Год 3018

12 апреля — Гэндальф приходит в Хоббитон.
20 июня — Саурон нападает на Осгилиат. Побег Голлума.
29 июня — Встреча Гэндальфа с Радагастом Бурым.
4 июля — Боромир выходит из Минас-Тирита.
10 июля — Гэндальф пленен Саруманом в Изенгарде.
Август — Все следы Горлума потеряны. Видимо он скрывается в Мории, находит дорогу к западным воротам, но не может их открыть.
18 сентября — Гэндальф покидает Изенгард. Черные Всадники пересекают Броды Изена.
19 сентября — Гэндальф приходит в Эдорас. Теоден велит ему уйти, позволив выбрать любого коня.
21 сентября — Маг выбирает Сполоха.
22 сентября — Черные Всадники достигают Сарнского брода и прорываются через заставу Следопытов. Гэндальф приручает Сполоха.
24 сентября — Гэндальф пересекает Изен.
26 сентября — Фродо попадает к Тому Бомбадилу.
27 сентября — Гэндальф пересекает Седонну. Фродо проводит у Тома Бомбадила вторую ночь.
28 сентября — Хоббиты в Упокоищах. Гэндальф у Сарнского Брода.
29 сентября — Фродо приезжает в Бри.
30 сентября — Рано утром совершаются нападения на Кривражки и на трактир в Бри. Фродо покидает Бри. К вечеру в Бри приезжает Гэндальф.
1 октября — Гэндальф покидает Бри.
3 октября — Ночью на Заветри он отбивает нападение Черных Всадников.
6 октября — Ночной налет на лагерь у Заветри. Фродо ранен.
9 октября — Глорфиндель выезжает из Имладриса.
11 октября — Глорфиндель встречается с Всадниками у моста через Седонну. Всадники отступают.
13 октября — Фродо переходит мост.
18 октября — Глорфиндель встречает Фродо. Гэндальф приезжает в Имладрис.
20 октября — Встреча с Черными Всадниками у Брода через Бруинен.
24 октября — Фродо просыпается в Имладрисе. Ночью приезжает Боромир.
25 октября — Совет у Элронда.
25 декабря — Отряд Хранителей покидает Имладрис.
Год 3019

11, 12 января — Отряд попадает в Снежную Бурю на Карадрасе
13 января — Перед рассветом нападение волколаков. Вечером отряд подходит к Западным Воротам Мории. Голлум начинает следить за отрядом.
15 января — Сражение Гэндальфа с Балрогом на мосту Казад-Дум. Гэндальф вместе с демоном падает в Морийскую Бездну. Отряд прорывается сквозь орды орков и выходит к Нимродели.
17 января — Отряд входит в Лориэн
23 января — Гэндальф преследует Балрога до вершины Зиракзигиль
25 января — Гэндальф побеждает Балрога и умирает.
14 февраля — Фродо и Сэм смотрят в Зеркало Галадриэли. Гэндальф возвращается к жизни.
16 февраля — Хранители покидают Лориэн. Голлум продолжает слежку.
17 февраля — Гваихир приносит Гэндальфа в Лориэн
23 февраля — орки ночью нападают на лодки хранителей
25 февраля — Отряд останавливается в Порт Галене. Сражение у Изенских Бродов, в котором погибает Теодред.
26 февраля — Отряд распался. Боромир убит. Мерри и Пин попадают в плен к урук-хай. Арагорн, Леголас и Гимли начинают за ними погоню. Эомеру докладывают об орде орков, спустившейся с Эмин Муил. Фродо и Сэм на восточных отрогах Эмин Муил.
27 февраля — Эомер, вопреки приказу Теодена, пускается в погоню за орками.
28 февраля — Эомер настигает орков возле леса Фангорн
29 февраля — Мерри и Пин убегают в лес Фангорн и встречают там Древоборода. Рохиррим уничтожают орду орков. Фродо и Сэм встречаются с Голлумом. Фарамиру видится погребальная лодка Боромира.
30 февраля — Начинается Совет Энтов. Эомер встречается с Арагорном, Леголасом и Гимли.
1 марта — Фродо идёт через Гиблые Болота. Арагорн, Леголас и Гимли встречается с Гэндальфом Белым. Они отправляются в Эдорас. Фарамир выходит из Минас Тирита на разведку в Итилиен.
2 марта — Фродо пересекает Болота. Гэндальф приходит в Эдорас и исцеляет Теодена. Рохиррим выступают против Сарумана. Вторая битва у Изенских Бродов. Поражение Эркенбранда. Оканчивается Совет Энтов. Энты выступают на Изенгард.
3 марта — Теоден приходит в Хельмову Падь. Начинается сражение у Хельмовой Пади. Энты разрушают Изенгард.
4 марта — Гэндальф и Теоден отправляются в Изенгард. Фродо и Сэм у пустошей Мораннона.
5 марта — Разговор с Саруманом в Ортанке. Над лагерем пролетает крылатый назгул. Гэндальф с Пиппином уезжают в Минас Тирит. Фродо и Сэм у врат Мораннона.
6 марта — Арагорн встречает отряд дунэдайн. Теоден выходит в Дунхарроу.
7 марта — Фарамир встречается с Фродо и Сэмом. Арагорн приезжает в Дунхарроу
8 марта — Арагорн вступает на Путь Мёртвых и в полночь достигает Камня Эреха. Фродо покидает Хеннет Аннун.
9 марта — Гэндальф приезжает в Минас Тирит. В сумерки Фродо и Сэм подходят к Моргульской Дороге. Теоден в Дунхарроу. Из Мордора поднимается тьма.
10 марта — Не рассвело. Роххирим выступают в поход. Гэндальф спасает Фарамира у врат Минас Тирита. Арагорн пересекает Рингло. Войска Мордора входят в Анориэн. Фродо и Сэм минуют Перекрёсток Дорог и смотрят на выход войск из Минас Моргула.
11 марта — Голлум встречается с Шелоб, потом видит Фродо спящим и едва не раскаивается. Дэнетор посылает Фарамира в Осгилиат. Арагорн в Лебеннине. Орки атакуют Лориэн и восточный Рохан.
12 марта — Голлум приводит Фродо в логово Шелоб. Арагорн идёт к Пеларгиру. Энты уничтожают орков, вторгшихся в Рохан.
13 марта — Фродо схвачен орками в Кирит Унголе. Пеленнор разрушен. Фарамир ранен. Арагорн врывается с Армией Мёртвых в Пеларгир и захватывает флот. Теоден в лесу Друэдайн.
14 марта — Сэм находит Фродо. Минас Тирит в осаде. Народ Друэдайн показывает роххирим дорогу к Минас Тириту.
15 марта — На рассвете Король-Чародей разбивает ворота Минас Тирита. Денетор сжигает себя на костре. Звучат рога рохиррим. Битва на Пеленноре. Пал Теоден. Эовин и Мерри повергают Короля-Чародея. Арагорн поднимает стяг Арвен. Фродо и Сэм уходят из крепости Кирит Унгол. Сражение в Лихолесье. Трандуил отбрасывает сила Дол Гулдура. Вторая атака на Лориэн.
16 марта — Совет военачальников. Фродо смотрит на Ородруин.
17 марта — Война на севере. Короли Бранд и Даин Железностоп погибают. Гномы и люди укрываются в Эреборе. Гора осаждена. Шаграт приносит плащ, кольчугу и меч Фродо в Барад Дур.
18 марта — Войска Запада выходят из Минас Тирита. Фродо и Сэм идут в колонне орков к Удуну.
19 марта — Войска Запада подходят к Моргульской Долине. Фродо и Сэм идут по дороге к Барад Дуру.
22 марта — Фродо и Сэм поворачивают к Роковой Горе.Третья атака на Лориэн.
23 марта — Войска Запада минуют Итилиен. Арагорн разрешает слабодушным вернутся. Фродо и Сэм оставляют лишние вещи, доспехи орков и оружие.
24 марта — Фродо и Сэм у подножия Ородруина. Войска Запада у Мораннона.
25 марта — Фродо и Сэм в Огненной Пещере. Голлум с Кольцом падает в недра вулкана. Конец Барад Дура. Конец Саурона.
После падения Саурона Тьма рассеялась, и войска Врага обуяли страх и отчаяние. Орки Дол-Гулдура трижды штурмовали Лориэн, но сила Благословенных Земель была столь велика, что без Саурона взять Лориен не удалось. Леса на границах сильно пострадали, но атаки были отбиты, а когда развеялась Завеса Тьмы, Келеборн во главе большого отряда переправился через Андуин и взял Дол-Гулдур. Галадриэль обрушила стены крепости. На севере также шла война. Враги вторглись во владения Трандуила, были большие пожары и разрушения, но в конце концов Трандуил одержал победу. В день Эльфийского Нового Года Келеборн и Трандуил встретились в сердце леса и переименовали Сумеречье в Эрин Ласгален, Ясный Лес. Северная его часть вплоть до лесного нагорья отошла к Владениям Трандуила, а южная стала зваться Восточным Лориеном. Срединные Леса отошли к Бнорнингам и лесовикам. Однако, когда Галадриэль ушла за Море, Келеборну наскучили его владения, и он удалился в Ривенделл, где ещё жили сыновья Элронда. Лесные Эльфы долго жили в Ясном Лесу, а вот Лориен скоро опустел.

Примерно в то время, когда был осажден Минас-Тирит, враги вторглись во владения Бранда. К нему на помощь пришли гномы из Эребора, и у подножия Горы была великая битва. Она продолжалась три дня и в ней пали короли Бранд и Даин Железностоп. Вастаки победили, но многие люди и гномы укрылись в Эреборе. Вести о великих победах на юге придали осажденным мужества и помогли разбить врагов. Из вастаков уцелели немногие. Они бежали на восток и больше не беспокоили Эсгарот. Королем стал Бард II, а Королём-под-Горой — Торин III Твердошлем, сын Даина. Их посольства присутствовали на коронации Короля Элессара, и в дальнейшем их владения пользовались его покровительством.

Даты после падения Барад Дура Править
Год 3019

27 марта — Бард II и Торин III Твердошлем оттесняют врагов от Эребора.
28 марта — Келеборн переходит Андуин. Штурм Дол Гулдура.
6 апреля — Встреча Келеборна и Трандуила.
9 апреля — Хранителей славят на лугах Кормаллена.
1 мая — Коронация Арагорна. Элронд и Арвен выезжают из Ривенделла.
8 мая — Эомер и Эовин отъезжают в Рохан с сыновьями Элронда.
20 мая — Элронд и Арвен приезжают в Лориэн.
27 мая — Свита Арвен покидает Лориэн.
14 июня — Сыновья Элронда встречают и сопровождают Арвен в Эдорас.
16 июня — Элронд с Арвен и сыновьями выезжают в Гондор.
25 июня —  Король Элессар находит молодое Белое Древо.
Врата Лета —  Арвен приезжает в Минас Тирит. Свадьба Арагорна и Арвен.
18 июля — Эомер возвращается в Минас Тирит.
19 июля — Погребальный поезд Теодена отправляется в Эдорас.
7 августа — Погребальный поезд прибывает в Эдорас.
10 августа — Похороны конунга Теодена
14 августа — Гости прощаются с конунгом Эомером.
22 августа — Они прибывают в Изенгард и прощаются с королём Элессаром.
28 августа — Они едут дальше и встречают Сарумана. Саруман поворачивает в Шир.
6 сентября — Мудрые и хоббиты возле Гор Мории.
13 сентября — Келеборн и Галадриэль расстаются с ними и направляются в Лориэн, остальные едут в Ривенделл.
21 сентября — Возвращение в Ривенделл.
22 сентября — Сто двадцать девятый день рождения Бильбо. Саруман приходит в Шир.
5 октября — Гэндальф и хоббиты покидают Ривенделл.
6 октября —  Гэндальф и хоббиты переправляются через Бруинен. Фродо нездоровится.
28 октября — Гэндальф и хоббиты вечером приезжают в Бри.
30 октября — Отъезд и Бри. К ночи путешественники достигают Брендидуиского моста.
1 ноября — Хоббитов арестовывают.
2 ноября — Хоббиты приходят в Уводье и поднимают восстание в Шире.
3 ноября —  Сражение в Уводье. Смерть Сарумана и Гримы.
Год 3020

13 марта — Фродо заболевает (годовщина ранения в логове Шелоб).
6 апреля — На праздничной поляне расцветает мэллорн.
1 мая — Свадьба Сэма и Рози.
Врата Лета — Фродо отказывается от должности мэра.
22 сентября — сто тридцатый день рождения Бильбо.
6 октября — Фродо снова болен (годовщина ранения на Амон Сул)
Год 3021 (последний год Т. Э.)

13 марта — Фродо снова болен.
25 марта — У Сэма родилась дочь Эланнор. В этот день по гондорскому летоисчислению начинается Четвёртая Эпоха.
21 сентября — Фродо и Сэм выезжают из Шира.
22 сентября — Они встречаются с остальными хранителями Кольца. Сто тридцать первый день рождения Бильбо.
29 сентября — Бильбо, Фродо, Гэндальф, Элронд и Галадриэль уплывают в Благословенный Край.
6 октября — Сэм возвращается в Шир.

----

TA 3018 - The Ringwraiths are given the task of retrieving the One Ring;
April 12, 3018 - Gandalf returns to the Shire telling Frodo Baggins he must take the ring away.
May 1, 3018 - Gandalf meets Aragorn at Sarn Ford to discuss Frodo's plan.
June 20, 3018 - Sauron attacks Osgiliath. Around the same time, Thranduil is attacked and Gollum escapes.
End of June, 3018 - Gandalf leaves the Shire for news in the south.
Mid-year's Day, 3018 - Gandalf writes a letter to Frodo from Bree.
July 4, 3018 - Boromir leaves Minas Tirith.
July 10, 3018 - Gandalf is arrested in Orthanc.
August 3018 - All traces of Gollum disappear. It is considered that, around this time, being hunted by elves and by the servants of Sauron, he could have taken refuge in Moria, but when he finally discovered the way to the West Gate, he couldn't leave.
September 18, 3018 - Gandalf escapes Orthanc in the first hours of the day. The Ringwraiths cross Isen.
September 19, 3018 - Gandalf goes to Edoras like a beggar, and his entrance is not allowed.
September 20, 3018 - Gandalf gains entry into Edoras. Théoden orders that he leaves: "Choose any horse, but leave before the end of the day of tomorrow!"
September 21, 3018 - Gandalf encounters Shadowfax, but the horse doesn't allow him to approach. Gandalf pursues Shadowfax for a long way in the hills.
September 22, 3018 - The Ringwraiths arrive at Sarn Ford at afternoon and drive away the rangers. Gandalf reaches Shadowfax.
September 23, 3018 - Four Ringwraiths enter the Shire before dawn. The others pursue the rangers eastward and later return to watch. A Ringwraith arrives in Hobbiton at nightfall. Frodo, Sam, and Pippin leave Bag End. Gandalf, having tamed Shadowfax, departs Rohan.
September 24, 3018 - Gandalf crosses the Isen. Frodo meets and travels with Gildor Inglorion of the House of Finrod in Green-hill country.
September 25, 3018 - Frodo spends the night at Crickhollow.
September 26, 3018 - Frodo, Sam, Pippin, and Merry enter the Old Forest and find Tom Bombadil.
September 27, 3018 - Second night with Bombadil.
September 28, 3018 - The hobbits are captured by a Barrow-wight. Gandalf reaches Sarn Ford.
September 29, 3018 - The hobbits arrive at Bree at nightfall. Gandalf visits The Gaffer. Aragorn meets Frodo in the Inn of the Prancing Pony.
September 30, 3018 - Aragorn leaves Bree with Frodo and company and they pass through the Chetwood.
October 1, 3018 - Gandalf leaves Bree.
October 2, 3018 - Aragorn and the hobbits enter the Midgewater Marshes.
October 3, 3018 - Gandalf is attacked during his night at Weathertop.
October 6, 3018 - The night at Weathertop. The Nazgûl locate Aragorn and the four hobbits. Frodo Baggins is hurt by a Morgul blade.
October 9, 3018 - Glorfindel leaves Rivendell tracking Frodo.
October 11, 3018 - Glorfindel expels the Ringwraiths from the Last Bridge.
October 13, 3018 - Aragorn and the hobbits cross the bridge.
October 14, 3018 - Glorfindel picks up the hobbits' trail west of the Hoarwell and follows them, while they climb through the Trollshaws.
October 18, 3018 - Frodo and company find the trolls that Bilbo met. Glorfindel finds Frodo in the afternoon. Gandalf arrives at Rivendell.
October 20, 3018 - Escape beyond Bruinen.
October 24, 3018 - Frodo awakes in the House of Elrond at Rivendell with Gandalf at his side. Boromir arrives at Rivendell by nightfall.
October 25, 3018 - Council of Elrond at Rivendell.
December 25, 3018 - The Fellowship of the Ring sets out in the evening.
January 8, 3019 - The Fellowship arrives at Hollin (Eregion).
January 11, 12, 3019 - Snow above Caradhras.
January 13, 3019 - Attack of wolves in the first hours of the day. The Fellowship arrives at the West Gate of Moria by nightfall. Gollum begins to follow the traces of the Ring-bearer.
January 14, 3019 - Night on the halls of Moria.
January 15, 3019 - The Fellowship parts after Gandalf falls into Khazad-dûm while fighting a Balrog.
January 17, 3019 - The Fellowship arrives at Caras Galadhon at evening.
January 23, 3019 - Gandalf pursues the balrog to the peak of Zirak-zigil.
January 25, 3019 - Gandalf slays the Balrog and dies. His body stays on the peak.
February 14, 3019 - The mirror of Galadriel. Gandalf returns to life.
February 16, 3019 - Farewell to Lórien. Gollum, hidden in the west margin, observes the departure.
February 17, 3019 - Gwaihir transports Gandalf to Lórien.
February 23, 3019 - The boats are attacked by night close to Sarn Gebir.
February 25, 3019 - The Fellowship passes by the Argonath and camps in Parth Galen. First Battle of the Fords of Isen. Théodred, King Théoden's son, slain in the battle.
February 26, 3019 - The Breaking of the Fellowship of the Ring. Death of Boromir; his horn is heard in Minas Tirith shortly before his death. Meriadoc Brandybuck and Peregrin Took are captured. Frodo and Samwise Gamgee penetrate the east part of Emyn Muil. Aragorn, Legolas and Gimli depart in pursuit of the orcs by night. Éomer knows of the descent of the band of orcs of Emyn Muil.
February 27, 3019 - Aragorn reaches the west cliff by sunrise. Éomer, against the orders of Théoden, departs the West Fold by midnight, pursuing the orcs.
February 28, 3019 - Éomer and the Rohirrim find the orcs around Fangorn Forest and slay them.
February 29, 3019 - Merry and Pippin escape and find Treebeard. Frodo and Sam find Gollum. Faramir finds the funerary boat of Boromir.
February 30, 3019 - The Entmoot begins. Éomer, returning to Edoras, encounters Aragorn.
March 1, 3019 - Frodo and Sam begin to cross the Dead Marshes at sunrise. The Entmoot continues. Aragorn finds Gandalf, the White. They depart for Edoras. Faramir leaves Minas Tirith and goes to Ithilien on a mission.
March 2, 3019 - Frodo and Sam arrive at the end of the Marshes. Gandalf arrives at Edoras and cures Théoden. The Rohirrim ride to the west and go against Saruman. The Second Battle of Isen. Erkenbrand defeated. Finish of the Entmoot by nightfall. The Ents march to Isengard, arriving there by midnight.
March 3, 3019 - Théoden goes to Helm's Deep. Beginning of the Battle of the Hornburg. The Ents complete the destruction of Isengard at 9 pm.
March 4, 3019 - The Battle of the Hornburg ends at dawn, when Gandalf arrives with Erkenbrand and the Rohirrim, killing the remaining Uruk-hai. Théoden and Gandalf ride to Isengard.
March 5, 3019 - Théoden arrives at Isengard by midday. Talking with Saruman in Orthanc. A Nazgûl upon his fell beast steed flies over the encampment in Dol Baran.
March 6, 3019 - Gandalf departs to Minas Tirith with Pippin. Frodo, Sam and Gollum hide close to the Morannon, and depart in twilight.
March 7, 3019 - Frodo and Sam are taken by Faramir to Henneth Annûn.
March 8, 3019 - Frodo departs Henneth Annûn.
March 9, 3019 - Gandalf arrives at Minas Tirith. Faramir departs from Henneth Annûn. Aragorn departs from Erech and arrives at Calembel. At twilight, Frodo, Sam and Gollum reach the Morgul road. The darkness of Mordor begins to spread.
March 10, 3019 - The Day without Dawn. The Concentration of the Troops of Rohan: the Rohirrim depart. Faramir rescued by Gandalf in the Gates of the City. An army of Morannon takes Cair Andros and invade Anórien. Frodo, Sam and Gollum watch the Army leaving Minas Morgul.
March 11, 3019 - Gollum visits Shelob but, seeing Frodo sleeping, is almost sorry. Denethor II sends Faramir to Osgiliath.
March 12, 3019 - Gollum takes Frodo to the "cave" of Shelob. Faramir flees to Minas Tirith after Osgiliath is overrun.
March 13, 3019 - Frodo, after escaping Shelob's cave, is attacked by Shelob and poisoned. Gollum, who wants the One Ring, attacks Sam.  Sam defeats him and Gollum escapes. Sam fights off Shelob, who flees wounded. Sam thinks that Frodo is dead and takes the One Ring. Frodo is captured by Orcs under the command of Shagrat and imprisoned in Cirith Ungol. The Pelennor Fields are invaded. Faramir is hurt.
March 14, 3019 - The Battle of the Pelennor Fields. Minas Tirith is enclosed by orc armies, who attack the city using catapults. The Nazgûl, under the command of the Witch-king of Angmar, and mounted on their fell beasts, attack the city from above. By nightfall, the powerful battering ram Grond tries to break the Gates of Minas Tirith.
March 15, 3019 - In the first hours of the day, Grond destroys the Gates of the City. Denethor, maddened, tries to burn himself and the wounded Faramir in a pyre. He orders the guards of the Citadel to bring him wood and oil. The horns of the rohirrim are heard at dawn: Théoden and his army arrive to help Gondor, killing thousands of orcs. Gandalf and Pippin save Faramir, but Denethor burns himself in the pyre. The Rohan army kills a great part of the orcs, including Lieutenant Gothmog. The surviving orcs are escorted to the river by Rohan's Army. Haradrim legions arrive with oliphaunts to help Mordor, and most of Rohan's army is annihilated. The Witch-king orders his fell beast to attack King Théoden. He drops to the ground and his horse crushes him. Dernhelm (revealed to be Eowyn) fights against the Witch-king's Fell Beast, and slays it in a single strike. The Witch-king is then slain by her and by Meriadoc Brandybuck. Aragorn, Legolas and Gimli arrive and kill the surviving orcs. Samwise rescues Frodo from the Tower of Cirith Ungol. The two finally reach Mordor.
March 16, 3019 - Debate of the commanders in Minas Tirith. Frodo observes Mount Doom.
March 18, 3019 - The West army under the command of Aragorn and Éomer depart Minas Tirith for the Black Gates of Mordor.
March 19, 3019 - The army arrives at the Morgul Vale. Frodo and Sam begin their journey to Mount Doom
March 22, 3019 - The terrible twilight. Frodo and Sam abandon the road and go to Mount Doom by the south.
March 23, 3019 - The Army leaves Ithilien. Aragorn dismisses the cowards. Frodo and Samwise get rid of their orc armor disguise.
March 24, 3019 - Frodo and Samwise makes their last journey to the roots of Mount Doom. The army camps in Morannon.
March 25, 3019 - The Battle of the Morannon. The army is enclosed by the much more numerous Orc army in the Black Gates. The Gondorian and Rohirrim army under the command of Aragorn, Éomer, Gandalf, Legolas and Gimli fights the orcs. While they fight, the eight remaining Nazgûl and their fell beasts arrive, but the Eagles also arrive to help Aragorn's army, battling the Nazgûl and their fell beasts. Frodo and Samwise, exhausted and starving, arrive at a doorway in Mount Doom. Gollum, supposedly dead, reappears and attacks Frodo and Sam. Sam fights Gollum, who stays behind while Frodo and he enter Mount Doom. When about to destroy the One Ring, Frodo stops, and puts on the ring, arguing that the Ring is his, and disappears. Sensing that the Ring was inside Mount Doom, Sauron's Eye looks there, and the three surviving Nazgûl fly to Mount Doom. Gollum takes the One Ring and falls in Mount Doom's lava, dying. The One Ring is destroyed (noon?). Sauron and his armies are destroyed. Frodo and Samwise are rescued from Mount Doom by Gandalf and the Eagles.
May 1, 3019 - Aragorn is crowned King Elessar of the Reunited Kingdom of Arnor and Gondor; Gandalf helps Aragorn to find the sapling of the new White Tree.
Mid-year's Day (between June and July) 3019 - Aragorn marries Arwen Undómiel.
July 3019 - King Théoden is laid to rest beside other Kings of Rohan in Edoras. Announcement of Faramir's and Éowyn's betrothal.
(Date unspecified) - Faramir marries Éowyn.
November 19, 3019 - Battle of Bywater; death of Saruman and Wormtongue; the end of the War of the Ring.
Spring 3020 - Samwise Gamgee marries Rosie Cotton and together they move to Bag End.
TA 3021 - Éomer marries Imrahil's daughter, Lothíriel of Dol Amroth.
September 22, 3021 - Bilbo marks his 131st birthday, surpassing the Old Took.
September 29, 3021 - Elrond, Galadriel, Gandalf, Frodo and Bilbo depart from the Grey Havens and go to the Undying Lands.
October 6, 3021 - Samwise returns to Bag End.
"""