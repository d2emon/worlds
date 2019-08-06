import logging


class Messages:
    def __init__(self):
        self.__is_clean = True
        self.__incomplete = False
        self.__in_process = False

        self.__prompt = ""
        self.cmd = ""

        self.log_fl = None
        self.snoopd = None
        self.snoopt = None
        self.sysbuf = None

        self.__messages = []

    def add(self, message):
        self.__messages.append(message)

    def add_buffer(self):
        closeworld()

        readers = []
        if self.log_fl is not None:
            readers.append({
                'reader': self.log_fl,
                'iskb': False,
            })
        if self.snoopd is not None:
            fln = opensnoop(self.snoopd.name, "a")
            if fln is not None:
                readers.append({
                    'reader': fln,
                    'iskb': False,
                    'on_read': lambda: fln.disconnect()
                })
        readers.append({'iskb': True})

        if len(self.sysbuf):
            self.output()
            for reader in readers:
                dcprnt(self.sysbuf, **reader)

            self.sysbuf = ""  # clear buffer

        if self.snoopt is not None:
            viewsnoop()

    def input(self, prompt, max_length):
        def after_input():
            self.__in_process = False

        self.__prompt = prompt
        self.cmd = ""

        self.__in_process = True

        self.add(prompt)
        self.add_buffer()

        self.__incomplete = False
        self.cmd = getchar(after_input)[:max_length]

    def output(self):
        if self.__incomplete:
            self.add("\n")

        self.__is_clean = False
        self.__incomplete = False

    def reprint(self):
        self.__incomplete = True
        self.add_buffer()

        if self.__is_clean or not self.__in_process:
            return

        self.add("\n{}{}".format(self.__prompt, self.cmd))

        self.__is_clean = True

    def stop(self):
        # So we dont get a prompt after the exit
        self.__is_clean = True


class Game:
    def __init__(self, name, user_ip=None):
        self.name = "The {}".format(name) if name == "Phantom" else name
        self.response = {}
        self.__active = False
        self.__on_timer = None
        self.__has_unread = False  # rd_qd

        self.messages = Messages()

        self.character = None
        self.character_id = None
        self.cms = None
        self.convflg = None
        self.curmode = None
        self.debug_mode = None
        self.fighting = None
        self.i_setup = None
        self.in_fight = None
        self.is_wizard = None
        self.maxu = None
        self.room_id = None
        self.zapped = None

        self.messages.add("Entering Game ....\n")
        logging.info("GAME ENTRY: %s[%s]", self.name, user_ip)
        self.messages.add("Hello {}\n".format(self.name))
        self.start()

    def start(self):
        makebfr()

        self.cms = -1
        putmeon(self.name)

        if openworld() is None:
            self.finish("Sorry AberMUD is currently unavailable")
        if self.character_id >= self.maxu:
            self.add_exit_message(0, "\nSorry AberMUD is full at the moment\n")
        rte(self.name)
        closeworld()

        self.cms = -1
        special(".g", self.name)
        self.i_setup = True

    def main(self):
        self.add_buffer()

        self.sendmsg()

        if self.__has_unread:
            rte(self.name)
            self.__has_unread = False

        closeworld()
        self.add_buffer()

    def finish(self, message):
        self.add_buffer()
        self.messages.stop()
        self.add_exit_message(0, message)

    def sendmsg(self):
        self.add_buffer()

        prmpt = ""
        if self.debug_mode:
            prmpt += "#"
        if self.is_wizard:
            prmpt += "----"
        if self.convflg == 0:
            prmpt += ">"
        elif self.convflg == 1:
            prmpt += "\""
        elif self.convflg == 2:
            prmpt += "*"
        else:
            prmpt += "?"
        if self.character.visible:
            prmpt = "({})".format(prmpt)

        self.add_buffer()

        if self.character.visible > 9999:
            set_progname("-csh")
        elif self.character.visible == 0:
            set_progname("   --}----- ABERMUD -----{--     Playing as {}".format(self.name))

        self.timer = True
        self.messages.input(prmpt, 80)
        self.timer = False

        self.messages.sysbuf.append("[l]{}[/l]".format(self.messages.cmd))

        openworld()
        rte(self.name)
        closeworld()

        if self.convflg and self.messages.cmd == "**":
            self.convflg = 0
            return self.sendmsg()

        if not self.messages.cmd:
            work = ""
        elif self.messages.cmd != "*" and self.messages.cmd[0] == "*":
            work = self.messages.cmd[1:]
        elif not self.convflg:
            work = self.messages.cmd
        elif self.convflg == 1:
            work = "say {}".format(self.messages.cmd)
        else:
            work = "tss {}".format(self.messages.cmd)

        if self.curmode:
            gamecom(work)
        else:
            if work and work not in (".q", ".Q"):
                a = special(work, self.name)

        if self.fighting is not None:
            if not self.fighting.exists or self.fighting.room_id != self.room_id:
                self.in_fight = 0
                self.fighting = None

        if self.in_fight:
            self.in_fight -= 1

        return work in (".Q", ".q")

    def loose(self):
        self.timer = False
        # No interruptions while you are busy dying
        # ABOUT 2 MINUTES OR SO

        self.i_setup = False

        openworld()
        dumpitems()
        if self.character.visible < 10000:
            sendsys(
                self.name,
                self.name,
                -10113,
                0,
                "{} has departed from AberMUDII\n".format(self.name)
            )
        self.character.remove()
        closeworld()

        if not self.zapped:
            saveme()

        chksnp()

    # Timer

    @property
    def timer(self):
        return self.__active

    @timer.setter
    def timer(self, value):
        self.__active = value
        self.__on_timer = self.on_timer if value else None

    # Response

    def add_buffer(self):
        timer = self.timer
        self.timer = False
        self.messages.add_buffer()
        self.timer = timer

    def add_exit_message(self, code, message=None):
        self.make_response({
            'exit': True,
            'code': code,
            'message': message,
        })

    def make_response(self, response):
        self.response.update(response)

    # Events

    def on_error(self):
        self.loose()
        self.add_exit_message(255)

    def on_exit(self):
        self.messages.add("^C\n")
        if self.in_fight:
            return

        self.loose()
        self.finish("Byeeeeeeeeee  ...........")

    def on_timer(self):
        if not self.timer:
            return

        self.timer = False
        openworld()
        rte(self.name, interrupt=True)
        on_timing()
        closeworld()

        self.messages.reprint()
        self.timer = True
