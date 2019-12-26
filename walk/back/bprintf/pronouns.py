def fpbns(player):
    return None


####


class Pronouns:
    def __init__(self):
        self.__pronouns = {
            'him': None,
            'her': None,
            'it': None,
            'them': None,
        }

    def set_name(self, player):
        if not player:
            return

        riatha = fpbns("riatha")
        shazareth = fpbns("shazareth")
        not_it = [p and p.name for p in (riatha, shazareth)]

        if player.player_id and player.player_id > 15 and player.player_id not in not_it:
            pronoun = 'it'
        elif player.sex:
            pronoun = 'her'
        else:
            pronoun = 'him'
        self.__pronouns[pronoun] = player.name

        if pronoun != 'it':
            self.__pronouns['them'] = player.name
