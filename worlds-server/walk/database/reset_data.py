import re
from .database import ListDatabase


class ResetData(ListDatabase):
    __VALUES = """
-1
0
0:0:0
0
-5
0			 /* These flags are byte flag 0 damage VVV*/
15:0:1000000000000000
0			/* Byte flag 1 unused */
-1071		      /* The 16 bit flags - uses can be found in code */
1
0:0:100010
0
-1072
1
0:0:100010
0
-1072
1
0:0:11000000000
0
-1072 candle 2nd
1
0:0:11000000000
0
-1072 candle 3
1
0:0:11000000000
0
173 ball
0
0:0:0
3
-1073 scroll
0
0:0:0
0
-1073 runes
0
0:0:0
0
-1075 candlestick
2
10:0:1000000000000000
0
-1074 cauldron
0
0:0:0
0
-1074 fire
0
0:0:0010011000000000
0
-1076 wand
0
8:0:1000000000000000
0
-1081 Ball of light
0
0:0:0010011000000000
0
-1081 bag of coins
0
5:0:1000000000000000
0
-1081 wand of fireballs
0
10:0:1000000000000000
0
-1081 gold orb
0
0:0:0
0
17 ring
0
0:0:100000000
1
-1079 sceptre
0
15:0:1000000000000000
0
-1081 door
1
0:0:1110
0
-1080 door
1
0:0:1110
0
-1071 book
1
0:0:1000000000000
0
-1080 hole in wall
0
0:0:0
0
-1056 torch on wall
0
0:0:0
0
-1066 key
0
0:0:100000000000
0
-1056 sec door
1
0:0:100010
0
-1070 door visible side
1
0:0:110
0
-1060 Pc
0
0:0:10
0
-1053 Pc
0
0:0:10
0
-1060 lever
0
0:0:0
0
-1061 shoe
0
0:0:0
0
-1056 Sword n stone
1
35:0:1001000000000000
0
-1066 sword
0
18:0:1000000000000000
0
-1066 dagger
0
14:0:1000000000000000
0
-600 knife
0
12:0:1000000000000000
0
-1065 maiden
0
0:0:110
0
-1069 maiden
0
0:0:110
0
-1059 throne
1
0:0:100010
0
-1062 throne
1
0:0:100010
0
-340 Pipes
0
0:0:0
-
-340 sporran
0
0:0:10000000
0
-342 claymore
0
25:0:1000000000000000
0
-309 bat
0
0:0:0
0
-620 rose
1
0:0:1000000000000
0
-633 cross
0
0:0:0
0
-644 roofing
0
0:0:0
0
-645 cock
0
0:0:0
0
-609 pitcher
0
0:0:0
0
-641 rope
0
0:0:0
0
-302
2
0:0:1110
0
-309 door
2
0:0:1110
0
-305 door
2
0:0:1110
0
-306 door
2
0:0:1110
0
-307 door
2
0:0:1110
0
-308 door
2
0:0:1110
0
-311 door
2
0:0:1110
0
-313 door
2
0:0:1110
0
-305 hammer
0
19:0:1000000000000000
0
-313 coin
0
0:0:0
0
-315 ale
0
0:0:1000000
0
-314 biscuit
0
0:0:1000000
0
-332 gate
0
0:0:10
0
-600 gate
0
0:0:10
0
-319 cutlery
0
0:0:0
0
-316 plate
0
0:0:0
0
-321 crystal
0
0:0:0
0
-320 axe
0
20:0:1000000000000000
0
-325 door
2
0:0:1110
0
-326 door
2
0:0:1110
0
-1064 pepper
0
0:0:1000000
0
-326 ruby
0
0:0:0
0
-326 sapphire
0
0:0:0
0
-326 diamond
0
0:0:0
0
-5 fire
0
0:0:10001000000000
0
-609 spring
0
0:0:0
0
-612 brand
1
6:0:1000011000000000
0
-637 brand
1
6:0:1000011000000000
0
-1051 plank
1
9:0:10000110000000000
0
-1081 fire
0
0:0:0010000000000000
0
-1081 potion
0
0:0:0
0
-1081 crown
0
0:0:0000000100000000
0
-643 key
0
0:0:100000000000
0
-1100 loaf
0
0:0:1000001
0
-1100 pie
0
0:0:1000001
0
-1100 bed
0
0:0:0
0
-614 apple
1
0:0:1000001000000
0
-1103 waybead
0
0:0:1000000
0
-1103 bread
0
0:0:1000000
0
-1102 shield
0
0:0:100000000
0
-1104 amulet
0
0:0:100000001
0
-1104 bedding
0
0:0:0
0
-1107 hammer
0
12:0:1000000000000000
0
-1108 rock
0
0:0:0
0
-1108 gem
0
0:0:1
0
-1112 pick
0
10:0:1000000000000000
0
-1112 ale
0
0:0:1000000
0
-1112 sarnies
0
0:0:1000000
0
-1118 nugget
0
0:0:0
0
-1123 nugget
0
0:0:0
0
-102 garlic
0
0:0:1000001
0
-128 robe
0
0:0:100000000
0
-104 rations
0
0:0:1000000
0
-104 rations
0
0:0:1000000
0
-107 statue
1
0:0:100010
0
-109 statue
1
0:0:10
0
-128 robe
0
0:0:100000000
0
-128 key
0
0:0:100000000001
0
-113 soap
0
0:0:0
0
-113 broom
0
0:0:0
0
-129 coffin
1
0:0:100000000000100
0
110 powerstone
0
0:0:0
3
-134 shield
0
0:0:0
0
-134 shield
0
0:0:100000001
0
-134 shield
0
0:0:100000001
0
-137 runes
0
0:0:0
0
-139 obsidian
0
0:0:0
0
-139 pumice
0
0:0:0
0
-133 lever
0
0:0:100011
0
-184 sack
0
0:0:100000000000000
0
-136 rod
0
0:0:0
0
-1    spare powerstone
0
0:0:0
0
-116 pillar
1
0:0:100010
0
-117 pillar
1
0:0:100010
0
-120 door
2
0:0:1110
0
-122 door
2
0:0:1110
0
-123 tripwire
0
0:0:0
0
-124 knife
0
7:0:1000000000000000
0
-125 door
2
0:0:1110
0
-127 door
2
0:0:1110
0
-127 ring
0
0:0:0
0
-142 boulder
0
0:0:0
0
-127 passage
1
0:0:10
0
-140 passage
1
0:0:10
0
-142 hole
1
0:0:10
0
-143 hole
1
0:0:10
0
-122 wand
0
0:0:10
0
-155 pit  (prob of slime word! - make vocab toggle on it )
1 /* 2 later ?*/
0:0:0
0
-156 lever
0
0:0:0
0
-190 flowers
0
0:0:100000000
0
-158 grille
1
0:0:110
0
-159 grille
1
0:0:10
0
-159 coins
0
0:0:0
0
-159 necklace
0
0:0:100000000
0
-153 tube
0
0:0:0
0
-153 scroll
0
0:0:1
0
-157 curtains
1
0:0:110
0
-160 curtains
1
0:0:110
0
-161 harp
0
0:0:0
0
-151 lever
0
0:0:0
0
-151 bridge
1
0:0:10
0
-149 bridge
1
0:0:10
0
-154 crys brid
0	/* 1 later */
0:0:10
0
-164 crys brid
0	/* 1 later */
0:0:10
0
-151 picture
0
0:0:0
0
-165 fire
0
0:0:10010000000000
0
-166 orb
0
0:0:0
0
-166 moonstone
0
0:0:0
0
-166 wand
0
0:0:0
0
-170 talisman
0
0:0:100000000
0
-161 giant
0
0:0:0
0
-128 robe
0
0:0:100000000
0
-131 bookcase
0
0:0:0
0
-131 stone
0
0:0:0
0
-131 book
0
0:0:0
0
-132 well
0
0:0:0
0
-184 fire
0
0:0:10010000000000
0
-187 branch
1
0:0:00011000000000
0
-184 poker
0
12:0:1000000000000000
0
-177 pick
0
11:0:1000000000000000
0
-180 stick
1
0:0:00011000000000
0
-190 stone
0
0:0:0
0
-190 scimitar
0
15:0:1000000000000000
0
-212 bag
0
0:0:100000000000000
0
-193 pendant
0
0:0:100000000
0
-194 pool
0
0:0:0
0
-192 hole
1
0:0:10
0
-172 hole
1
0:0:10
0
-196 cupboard
2
0:0:1110
0
-197 cupboard
2
0:0:1110
0
-197 chest
1
0:0:100000000000110
0
180 clasp
0
0:0:100000000
3
183 key
0
0:0:100000000000
3
-196 pillow
0
0:0:100000000000000
0
-194 ice dagger
0
18:0:1000000000000000
0
-109 gem
0
0:0:0
0
-651   slab top
1
0:0:111
0
-650 slab bottom
1
0:0:10
0
-650 wreath
0
0:0:100000000
0
-650 silk shroud
0
0:0:100000000
0
-109 effigy
0
0:0:0
0
-109 statue
0
0:0:0
0
-1079 chute top
0
0:0:0
0
-1076 chute bottom
0
0:0:0
0
    """.split("\n")[1:-1]

    @classmethod
    def __parse(cls, values):
        def bool_values(v):
            f = [c != '0' for c in value]
            return [f[i] if i < len(f) else False for i in range(16)]

        def int_value(s):
            match = re.search(r'-?\d+', s)
            return int(match.group() if match else 0)

        def flags(s):
            lowest, v, highest = s.split(':')
            return {
                'highest': bool_values(highest),  # highest bits
                'lowest': int_value(lowest),  # Chars in lowest 16 bits
                'value': int_value(v),
            }

        for value in values:
            yield {
                'room_id': int_value(value),
                1: int_value(next(values)),
                'flags': flags(next(values)),
                3: int_value(next(values)),
            }

    def reset(self):
        # a = connect(names.ob_in)
        return self.__parse((value for value in self.__VALUES))
