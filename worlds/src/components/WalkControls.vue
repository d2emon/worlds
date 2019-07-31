<template>
  <v-card>
    <v-dialog
      v-model="showingMessage"
      max-width="300"
    >
      <v-card>
        <v-card-text>
          {{message}}
        </v-card-text>
        <v-card-actions>
          <v-spacer />
          <v-btn
            text
            @click="hideMessage"
          >
            Ok
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-container>
      <v-layout row wrap>
        <v-flex xs3 class="offset-xs3">
          <v-btn flat icon>N</v-btn>
        </v-flex>
        <v-flex xs3 class="offset-xs3">
          <v-btn flat icon>U</v-btn>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs3>
          <v-btn flat icon>W</v-btn>
        </v-flex>
        <v-flex xs3 class="offset-xs3">
          <v-btn flat icon>E</v-btn>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-flex xs3 class="offset-xs3">
          <v-btn flat icon>S</v-btn>
        </v-flex>
        <v-flex xs3 class="offset-xs3">
          <v-btn flat icon>D</v-btn>
        </v-flex>
      </v-layout>
      <v-layout row wrap>
        <v-btn @click="setLevel(1)">Player</v-btn>
        <v-btn @click="setLevel(10)">Wizard</v-btn>
        <v-btn @click="setLevel(10000)">God</v-btn>
      </v-layout>
      <v-layout row wrap>
        <v-btn
          v-if="!inFight"
          @click="console.log(1)"
        >
          Go
        </v-btn>
        <v-btn
          v-else
          :disabled="!inFight"
          @click="doFlee"
        >
          Flee
        </v-btn>

        <v-btn
          :disabled="inFight || isForced"
          @click="doQuit"
        >
          Quit
        </v-btn>
        <v-btn @click="console.log(9)">Take</v-btn>
        <v-btn @click="console.log(10)">Drop</v-btn>

        <v-btn
          @click="getRoom"
        >
          Look
        </v-btn>
        <v-btn @click="console.log(12)">Inventory</v-btn>
        <v-btn @click="console.log(13)">Who</v-btn>
        <v-btn @click="console.log(14)">Reset</v-btn>
        <v-btn @click="console.log(15)">Zap</v-btn>
        <v-btn @click="console.log(16)">Eat</v-btn>
        <v-btn @click="console.log(17)">Play</v-btn>
        <v-btn @click="console.log(18)">Shout</v-btn>
        <v-btn @click="console.log(19)">Say</v-btn>
        <v-btn @click="console.log(20)">Tell</v-btn>

        <v-btn @click="console.log(21)">Save</v-btn>
        <v-btn @click="console.log(22)">Score</v-btn>
        <v-btn @click="console.log(23)">Exorcise</v-btn>
        <v-btn @click="console.log(24)">Give</v-btn>
        <v-btn @click="console.log(25)">Steal</v-btn>
        <v-btn @click="console.log(26)">Levels</v-btn>
        <v-btn @click="console.log(27)">Help</v-btn>
        <v-btn @click="console.log(28)">Value</v-btn>
        <v-btn @click="console.log(29)">Stats</v-btn>
        <v-btn @click="console.log(30)">Examine</v-btn>

        <v-btn @click="console.log(31)">Delete</v-btn>
        <v-btn @click="console.log(32)">Password</v-btn>
        <v-btn @click="console.log(33)">Summon</v-btn>
        <v-btn @click="console.log(34)">Wield</v-btn>
        <v-btn @click="console.log(35)">Kill</v-btn>

        <v-btn @click="console.log(50)">Laugh</v-btn>

        <v-btn @click="console.log(51)">Cry</v-btn>
        <v-btn @click="console.log(52)">Burp</v-btn>
        <v-btn @click="console.log(53)">Fart</v-btn>
        <v-btn @click="console.log(54)">Hiccup</v-btn>
        <v-btn @click="console.log(55)">Grin</v-btn>
        <v-btn @click="console.log(56)">Smile</v-btn>
        <v-btn @click="console.log(57)">Wink</v-btn>
        <v-btn @click="console.log(58)">Snigger</v-btn>
        <v-btn @click="console.log(59)">Pose</v-btn>
        <v-btn @click="console.log(60)">Set</v-btn>

        <v-btn @click="console.log(61)">Pray</v-btn>
        <v-btn @click="console.log(62)">Storm</v-btn>
        <v-btn @click="console.log(63)">Rain</v-btn>
        <v-btn @click="console.log(64)">Sun</v-btn>
        <v-btn @click="console.log(65)">Snow</v-btn>
        <v-btn @click="console.log(66)">Go to</v-btn>

        <v-btn @click="console.log(100)">Wear</v-btn>

        <v-btn @click="console.log(101)">Remove</v-btn>
        <v-btn @click="console.log(102)">Put</v-btn>
        <v-btn @click="console.log(103)">Wave</v-btn>
        <v-btn @click="console.log(104)">Blizzard</v-btn>
        <v-btn @click="console.log(105)">Open</v-btn>
        <v-btn @click="console.log(106)">Close</v-btn>
        <v-btn @click="console.log(107)">Lock</v-btn>
        <v-btn @click="console.log(108)">Unlock</v-btn>
        <v-btn @click="console.log(109)">Force</v-btn>
        <v-btn @click="console.log(110)">Light</v-btn>

        <v-btn @click="console.log(111)">Extinguish</v-btn>
        <v-btn @click="console.log(112)">Where</v-btn>
        <v-btn @click="console.log(114)">Invisible</v-btn>
        <v-btn @click="console.log(115)">Visible</v-btn>
        <v-btn @click="console.log(117)">Push</v-btn>
        <v-btn @click="console.log(118)">Cripple</v-btn>
        <v-btn @click="console.log(119)">Cure</v-btn>
        <v-btn @click="console.log(120)">Dumb</v-btn>

        <v-btn @click="console.log(121)">Change</v-btn>
        <v-btn @click="console.log(122)">Missile</v-btn>
        <v-btn @click="console.log(123)">Shock</v-btn>
        <v-btn @click="console.log(124)">Fireball</v-btn>
        <v-btn @click="console.log(125)">Translocate</v-btn>
        <v-btn @click="console.log(126)">Blow</v-btn>
        <v-btn @click="console.log(127)">Sigh</v-btn>
        <v-btn @click="console.log(128)">Kiss</v-btn>
        <v-btn @click="console.log(129)">Hug</v-btn>
        <v-btn @click="console.log(130)">Slap</v-btn>

        <v-btn @click="console.log(131)">Tickle</v-btn>
        <v-btn @click="console.log(132)">Scream</v-btn>
        <v-btn @click="console.log(133)">Bounce</v-btn>
        <v-btn @click="console.log(134)">Wiz</v-btn>
        <v-btn @click="console.log(135)">Stare</v-btn>
        <v-btn @click="console.log(136)">Exits</v-btn>
        <v-btn @click="console.log(137)">Crash</v-btn>
        <v-btn @click="console.log(138)">Sing</v-btn>
        <v-btn
          :disabled="inFight"
          @click="console.log(139)"
        >
          Grope
        </v-btn>
        <v-btn @click="console.log(140)">Spray</v-btn>

        <v-btn @click="console.log(141)">Groan</v-btn>
        <v-btn @click="console.log(142)">Moan</v-btn>
        <v-btn @click="console.log(143)">Directory</v-btn>
        <v-btn @click="console.log(144)">Yawn</v-btn>
        <v-btn @click="console.log(145)">Wizlist</v-btn>
        <v-btn @click="console.log(146)">In</v-btn>
        <v-btn @click="console.log(147)">Smoke</v-btn>
        <v-btn @click="console.log(148)">Deafen</v-btn>
        <v-btn @click="console.log(149)">Ressurect</v-btn>
        <v-btn @click="console.log(150)">Log</v-btn>

        <v-btn @click="console.log(151)">Tss</v-btn>
        <v-btn @click="console.log(152)">Remote Editor</v-btn>
        <v-btn @click="console.log(153)">Loc</v-btn>
        <v-btn @click="console.log(154)">Squeeze</v-btn>
        <v-btn @click="console.log(155)">Users</v-btn>
        <v-btn @click="console.log(156)">Honeyboard</v-btn>
        <v-btn @click="console.log(157)">INumber</v-btn>
        <v-btn @click="console.log(158)">Update</v-btn>
        <v-btn @click="console.log(159)">Become</v-btn>
        <v-btn @click="console.log(160)">Systat</v-btn>

        <v-btn @click="console.log(161)">Converse</v-btn>
        <v-btn @click="console.log(162)">Snoop</v-btn>
        <v-btn @click="console.log(163)">Shell</v-btn>
        <v-btn @click="console.log(164)">Raw</v-btn>
        <v-btn @click="console.log(165)">Purr</v-btn>
        <v-btn @click="console.log(166)">Cuddle</v-btn>
        <v-btn @click="console.log(167)">Sulk</v-btn>
        <v-btn @click="console.log(168)">Roll</v-btn>
        <v-btn
          @click="doCredits"
        >
          Credits
        </v-btn>
        <v-switch
          label="Brief"
          :input-value="brief"
          @change="setBrief"
        />

        <v-btn @click="console.log(171)">Debug</v-btn>
        <v-btn @click="console.log(172)">Jump</v-btn>
        <v-btn
          @click="doMap"
        >
          Map
        </v-btn>
        <v-btn @click="console.log(175)">Bug</v-btn>
        <v-btn @click="console.log(176)">Typo</v-btn>
        <v-btn @click="console.log(177)">Pn</v-btn>
        <v-btn @click="console.log(178)">Blind</v-btn>
        <v-btn @click="console.log(179)">Patch</v-btn>
        <v-switch
          label="Debug Mode"
          :input-value="debugMode"
          @change="setDebugMode"
        />

        <v-btn @click="console.log(181)">PFlags</v-btn>
        <v-btn @click="console.log(182)">Frobnicate</v-btn>
        <v-btn @click="console.log(183)">Set In</v-btn>
        <v-btn @click="console.log(184)">Set Out</v-btn>
        <v-btn @click="console.log(185)">Set Magic In</v-btn>
        <v-btn @click="console.log(186)">Set Magic Out</v-btn>
        <v-btn @click="console.log(187)">Emote</v-btn>
        <v-btn @click="console.log(188)">Dig</v-btn>
        <v-btn @click="console.log(189)">Empty</v-btn>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
import {
  mapState,
  mapGetters,
  mapMutations,
  mapActions,
} from 'vuex';

export default {
  name: 'WalkControls',
  computed: {
    ...mapGetters('walk', [
      'showingMessage',
      'isDebugger',
    ]),
    ...mapState('walk', [
      'message',
      'brief',
      'debugMode',
      'player',
    ]),
  },
  data: () => ({
    level: 1,

    // Special
    inFight: false,
    isForced: false,
    globme: 'Globme',
    curch: -1,
    curmode: 0,
    mynum: 1,
    my_sco: 0,
    debugMode: false,
  }),
  methods: {
    ...mapMutations('walk', [
      'setBrief',
    ]),
    ...mapActions('walk', [
      'showMessage',
      'hideMessage',
      'getRoom',
      'setDebugMode',
    ]),
    setLevel(level) {
      this.level = level;
    },
    // utils
    calibme: console.log,
    closeworld: console.log,
    crapup(message) { this.message = message; },
    dumpitems: console.log,
    iscarrby: console.log,
    on_flee_event: console.log,
    openworld: console.log,
    ptstflg: console.log,
    rte: console.log,
    saveme: console.log,
    sendsys: console.log,
    setpname: console.log,
    setpstr: console.log,
    // actions
    doGo() {
      console.log('go');
    },
    doQuit() {
      if (this.isForced) {
        return this.showMessage({ message: 'You can\'t be forced to do that\n' });
      }
      this.rte(this.globme);
      this.openworld();
      if (this.inFight) {
        return this.showMessage({ message: 'Not in the middle of a fight!\n' });
      }
      this.sendsys(
        this.globme,
        this.globme,
        -10000,
        this.curch,
        `${this.globme} has left the game\n`,
      );
      this.sendsys(
        this.globme,
        this.globme,
        -10113,
        this.curch,
        `[ Quitting Game : ${this.globme} ]\n`,
      );
      this.dumpitems();
      this.setpstr(this.mynum, -1);
      this.setpname(this.mynum, '');
      this.closeworld();

      this.curmode = 0;
      this.curch = 0;

      this.saveme();

      this.showMessage({
        message: 'Ok',
        onMessage: () => this.crapup('Goodbye'),
      });
    },
    doCredits() {
      return this.showMessage({ message: '[file]CREDITS[/file]' });
    },
    doMap() {
      return this.showMessage({
        message: 'Your adventurers automatic monster detecting radar, and long range\n'
          + 'mapping kit, is, sadly, out of order.',
      });
    },
    doFlee() {
      if (!this.inFight) return this.doGo();
      if (this.iscarrby(32, this.mynum)) {
        return this.showMessage({ message: 'The sword won\'t let you!!!!' });
      }
      this.sendsys(
        this.globme,
        this.globme,
        -10000,
        this.curch,
        `[c]${this.globme}[/c] drops everything in a frantic attempt to escape\n`,
      );
      this.sendsys(
        this.globme,
        this.globme,
        -20000,
        this.curch,
        '',
      );
      this.my_sco -= this.my_sco / 33; // loose 3%
      this.calibme();
      this.inFight = false;
      this.on_flee_event();
      return this.doGo();
    },
  },
};
</script>

<style scoped>

</style>
