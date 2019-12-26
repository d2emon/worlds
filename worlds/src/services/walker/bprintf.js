import {
  error,
} from './crapup';
import {
  getState,
  setState,
} from './state';
import {
  getPlayer,
  saveWorld,
} from './world';
import {
  loose,
} from './player';
import {
  findPlayer,
  findPlayerVisible,
} from './objsys';
import {
  isDark,
} from './utils/room';
import {
  listFile,
} from './utils';

const sendMessage = message => new Promise(() => {
  if (message.length > 255) {
    console.error('Bprintf Short Buffer overflow');
    return error('Internal Error in BPRINTF');
  }

  const messages = [
    ...(getState().messages || []),
    message,
  ];

  if (messages.length > 4095) {
    console.error(`Buffer overflow on user ${getState().name}`);
    return loose()
      .then(() => error('PANIC - Buffer overflow'));
  }

  return setState({ messages });
});

const addMessage = message => sendMessage(message);

export default addMessage;

export const seePlayer = (player) => {
  const state = getState();
  const me = getPlayer(state.playerId);

  if (!me) {
    return false;
  }
  if (!player) {
    return true;
  }
  if (me.playerId === player.playerId) {
    return true;
  }
  if (me.level < player.visible) {
    return false;
  }
  if (state.ailBlind) {
    return false;
  }
  if ((state.channel === player.location) && isDark(state.channel)) {
    return false;
  }
  return true;
};

export const lookPlayer = async (player) => {
  const see = seePlayer(player);
  const { playerId } = getState();

  if (
    see
      && player
      && (player.playerId !== playerId)
  ) {
    await setState(setName(player.playerId));
  }
  return see;
};

const lookPlayerName = name => {
  const player = findPlayer(name);
  return player && lookPlayer(player);
};

// Specials
export const fromFile = message => `[f]${message}[/f]`;
export const audial = message => `[d]${message}[/d]`;
export const visual = (name, message) => `[s name="${name}"]${message}[/s]`;
export const playerVisible = message => `[p]${message}[/p]`;
export const dark = message => `[c]${message}[/c]`;
export const playerDeaf = message => `[P]${message}[/P]`;
export const playerBlind = message => `[D]${message}[/D]`;
export const fromKeyboard = message => `[l]${message}[/l]`;

const pfile = (match, filename) => {
  const { debugMode } = getState();
  const content = listFile(filename);
  return debugMode
    ? `[FILE ${filename} ]\n${content}`
    : content;
};

const pndeaf = (match, message) => !getState().ailDeaf ? message : '';

const pcansee = (match, name, message) => lookPlayerName(name) ? message : '';

const prname = (match, name) => lookPlayerName(name) ? name : 'Someone';

const pndark = (match, message) => (!isDark() && ! getState().ailBlind) ? message : '';

const ppndeaf = (match, name) => {
  if (getState().ailDeaf) {
    return '';
  }
  return lookPlayerName(name) ? name : 'Someone';
};

const ppnblind = (match, message) => {
  if (getState().ailBlind) {
    return '';
  }
  return lookPlayerName(name) ? name : 'Someone';
};

const pnotkb = isKeyboard => (match, message) => (!isKeyboard) ? message : '';

export const showFile = filename => `[f]${filename}[/f]`;
export const audio = message => `[d]${message}[/d]`;
export const visual = (player, message) => `[s name=\"${player}\"]${message}[/s]`;
export const visualName = player => `[p]${player}[/p]`;
export const notDark = message => `[c]${message}[/c]`;
export const notDeafName = player => `[P]${player}[/P]`;
export const notBlindName = player => `[D]${player}[/D]`;
export const notKeyboard = message => `[l]${message}[/l]`;

const applySpecial = (message, isKeyboard=true) => message
  .replace(/\[f\]([^\[]{0,128})\[\/f\]/g, pfile)
  .replace(/\[d\]([^\[]{0,256})\[\/d\]/g, pndeaf)
  .replace(/\[s name=\"([^\"]{0,23})\"\]([^\[]{0,256})\[\/s\]/g, pcansee)
  .replace(/\[p\]([^\[]{0,24})\[\/p\]/g, prname)
  .replace(/\[c\]([^\[]{0,256})\[\/c\]/g, pndark)
  .replace(/\[P\]([^\[]{0,24})\[\/P\]/g, ppndeaf)
  .replace(/\[D\]([^\[]{0,24})\[\/D\]/g, ppnblind)
  .replace(/\[l\]([^\[]{0,127})\[\/l\]/g, pnotkb(isKeyboard));

export const makeBuffer = () => setState({ messages: [] });

export const logcom = () => Promise.resolve()
  .then(() => {
    if (getuid() !== geteuid()) {
      throw new Error('Not allowed from this ID');
    }

    const {
      logFl,
    } = getState();

    if (logFl) {
      return fprintf(logFl, '\nEnd of log....\n\n')
        .then(fclose)
        .then(() => setState({ logFl: null }))
        .then(() => bprintf('End of log'));
    }

    bprintf('Commencing Logging Of Session\n');
    return Promise.resolve()
      .then(() => setState({
        logFl: fopen('mud_log', 'a'),
      }))
      .catch(() => setState({
        logFl: fopen('mud_log', 'w'),
      }))
      .catch(() => throw new Error('Cannot open log file mud_log'))
      .then(() => bprintf('The log will be written to the file \'mud_log\''));
  })
  .catch(e => bprintf(e.message));

export const showMessages = () => Promise.resolve(blockAlarm())
  .then(saveWorld)
  .then(() => {
    const {
      messages,
    } = getState();
    return (messages.length > 0) && setState({prDue: true});
  })
  .then((state) => {
    const {
      messages,
      prQcr,
    } = getState();
    if (messages.length > 0 && prQcr) {
      console.log('\n');
    }
    return setState({ prQcr: false });
  })
  .then((state) => {
    const {
      messages,
      logFl,
      snoopTarget,
      snoopDestination,
    } = getState();
    const promise = Promise.resolve();
    if (logFl) {
      promise
        .then(() => applySpecial(messages, logFl, false))
    }
    if (state.snoopDestination) {
      promise
        .then(() => {
          const player = getPlayer(snoopDestination);
          return player && opensnoop(player.name, 'a');
        })
        .then((fln) => Promise.resolve()
          .then(() => applySpecial(messages, fln, false))
          .then(fcloselock)
        )
        .catch(() => {});
    }
    promise
      .then(() => applySpecial(messages, null, true))
      .then(makeBuffer)
      .then(() => snoopTarget && viewsnoop());
  })
  .then(() => unblockAlarm());


const opensnoop = (player, permissions) => openlock(`${SNOOP}${player}`, permissions);

const snoopcom = (arg=null) => Promise.resolve()
  .then(() => {
    const {
      level,
      snoopTargetName,
      snoopTarget
    } = getState();

    if (level < 10) {
      throw new Error('Ho hum, the weather is nice isn\'t it');
    }
    if (snoopTarget) {
      bprintf(`Stopped snooping on ${snoopTargetName}`)
      setState({
        snoopTarget: null,
      })
        .then((s) => sendsys(
          s.snoopTargetName,
          s.name,
          -400,
          0,
          null,
        ))
    }
    if (!arg) {
      return Promise.resolve();
    }

    const x = findPlayerVisible(arg);
    if (!x) {
      throw new Error('Who is that?');
    }
    if (((level < 10000) && (x.level >= 10)) || (x.bit[6])) {
      return setState({
        snoopTarget: null,
      })
        .then(() => throw new Error('Your magical vision is obscured'))
    }
    return setState({
      snoopTargetName: x.name,
      snoopTarget: x.playerId,
    })
      .then((s) => {
        bprintf(`Started to snoop on ${x.name}`);
        return sendsys(
          s.snoopTargetName,
          s.name,
          -401,
          0,
          null,
        );
      })
      .then(() => opensnoop(getState().name, 'w'))
      .then(fx => fprintf(fx, ' '))
      .then(fcloselock);
  })
  .catch(e => bprintf(e.message));

const viewsnoop = () => opensnoop(getState().name, 'r+')
  .then((fx) => {
    if (!getState().snoopTarget) {
      return fx;
    }
    fx.forEach(z => console.log(`|${z}`));
    return fx;
  })
  .then(ftruncate)
  .then(fcloselock)
  .catch(() => {});

export const chksnp = () => getState().snoopTarget && sendsys(
  getState().snoopTargetName,
  getState().name,
  -400,
  0,
  null,
);
