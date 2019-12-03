class Timer:
    def __init__(self, on_timer=lambda: None):
        self.__time = None
        self.__is_active = False
        self.__has_alarm = False
        self.__on_timer = on_timer

    @property
    def has_alarm(self):
        return self.__has_alarm

    @has_alarm.setter
    def has_alarm(self, value):
        self.__has_alarm = value
        if self.is_active:
            self.__time = 2

    @property
    def is_active(self):
        return self.__is_active

    @is_active.setter
    def is_active(self, value):
        self.__is_active = value
        self.has_alarm = value
        if not value:
            self.__time = None

    def on_timer(self):
        if not self.is_active or not self.has_alarm:
            return

        self.is_active = False
        self.__on_timer()
        self.is_active = True
