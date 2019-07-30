from .actions import execute_action


class Globals:
    globme = ""
    my_lev = 0


class ParseError(Exception):
    pass


class Parser:
    last_text = ""

    verbtxt = []
    verbnum = []
    """
    char *verbtxt[]={"go","climb","n","e","s","w","u","d",
        "north","east","south","west","up","down",
        "quit",
        "get","take","drop","look","i","inv","inventory","who",
        "reset","zap","eat","drink","play",
        "shout","say","tell","save","score"
        ,"exorcise","give","steal","pinch","levels","help","value"
        ,"stats","examine","read","delete","pass","password",
        "summon","weapon","shoot","kill","hit","fire","launch","smash","break",
        "laugh","cry","burp","fart","hiccup","grin","smile","wink","snigger"
        ,"pose","set","pray","storm","rain","sun","snow","goto",
        "wear","remove","put","wave","blizzard","open","close",
        "shut","lock","unlock","force","light","extinguish","where","turn",
        "invisible","visible","pull","press","push","cripple","cure","dumb",
        "change","missile","shock","fireball","translocate","blow",
        "sigh","kiss","hug","slap","tickle","scream","bounce","wiz"
        ,"stare","exits","crash","sing","grope","spray"
        ,"groan","moan","directory","yawn","wizlist","in","smoke"
        ,"deafen","resurrect","log","tss","rmedit","loc","squeeze","users"
        ,"honeyboard","inumber","update","become","systat","converse"
        ,"snoop","shell","raw","purr","cuddle","sulk","roll","credits"
        ,"brief","debug","jump","wield","map","flee","bug","typo","pn"
        ,"blind","patch","debugmode","pflags","frobnicate","strike"
        ,"setin","setout","setmin","setmout","emote","dig","empty"
        ,0 };
    int verbnum[]={1,1,2,3,4,5,6,7,2,3,4,5,6,7,8,9,9,10,11,12,12,12,13,14
        ,15,16,16,17,18,19,20,21,22,23,24,25,25,26,27,28,29,30,30,31,32,32,33,34,35,35,35,35,35
        ,35,35,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66
        ,100,101,102,103,104,105,106,106,107,108,109,110,111,112,117,114,115,117,117,117
        ,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133
        ,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149
        ,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170
        ,171,172,34,173,174,175,176,177,178,179,180,181,182,35,183,184,185,186,187,188,189};
    """

    def __init__(self, text):
        self.wd_it = ""
        self.wd_him = ""
        self.wd_her = ""
        self.wd_them = ""
        self.wd_there = ""

        self.pos = 0  # stp
        self.text = text if text != "!" else self.last_text  # strbuf
        self.last_text = self.text
        self.word = ""  # wordbuf

    def pronoun(self, pronoun):
        return {
            'it': self.wd_it,
            'them': self.wd_them,
            'him': self.wd_him,
            'her': self.wd_her,
            'me': Globals.globme,
            'myself': Globals.globme,
            'there': self.wd_there,
        }.get(pronoun)

    def __iter__(self):
        return self

    def __next__(self):
        word = ""
        for self.pos in range(self.pos, len(self.text)):
            c = self.text[self.pos]
            if not len(word):
                if c == ' ':
                    continue
            if c == ' ':
                break
            word += c

        if not len(word):
            self.word = word

        self.word = self.word.lower()
        replace = self.pronoun(self.word)
        if replace is not None:
            self.word = replace

        return self.word if len(word) else None

    def parse(self):
        word = next(self)
        if word is None:
            raise ParseError("Pardon?")

        a = check_verb()
        if a is None:
            raise ParseError("I don't know that verb")
        return a

    def check_verb(self):
        return check_list(self.word, self.verbtxt, self.verbnum)


PARSER = Parser("")


def check_list(word, src, dst):
    word = word.lower()
    diff = [(dst[item_id], word_diff(word, item)) for (item_id, item) in enumerate(src)]
    item, best = max(diff, key=lambda item: item[2])
    return None if best < 5 else item


def check_verb():
    return PARSER.check_verb()


def word_diff(x, y):
    if x == y:
        return 10000
    if y == "reset":
        return -1
    if not x:
        return 0

    weights = {
        0: 3,
        1: 2,
    }

    return sum(
        weights.get(n, 1)
        for n in range(min(len(x), len(y)))
        if x[n] == y[n]
    )


def parse(text):
    if not text or text == ".q":
        return

    action_id = Parser(text).parse()
    return execute_action(action_id)


def next_word():
    return next(PARSER)
