from back import get_can_exit, get_loose, get_timer, post_start
from output import Output
from timer import Timer


class State:
    title = ""

    name = ''
    in_fight = 0


class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.__username = username

    @property
    def username(self):
        return "The " + self.__username if self.__username == "Phantom" else self.__username


class Gui:
    def __init__(self, title, user):
        self.timer = Timer(on_timer=self.on_timer)
        self.output = Output(without_alarm=self.timer.without_alarm)

        State.title = title
        State.name = user.username

        print('Entering Game ....')
        result = post_start(user.user_id, user.username)
        print(result.get('message'))

    def on_timer(self):
        get_timer(State.name)
        self.output.reprint()

    def on_error(self, error):
        self.timer.is_active = False
        self.loseme(str(error))

    def on_exit(self):
        print("^C")
        if not get_can_exit():
            return
        self.on_error(Exception("Byeeeeeeeeee  ..........."))

    def loseme(self, message=None):
        get_loose()
        if message:
            self.output.error(message)


def main(title, user_id, username):
    Gui(title, User(user_id, username))
