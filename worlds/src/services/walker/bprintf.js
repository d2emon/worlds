import {
  error,
} from './crapup';
import {getState, setState} from "./state";
import {getPlayer, saveWorld, setPlayer} from "./world";
import {loose} from "./player";
import {findPlayerVisible} from "./objsys";

const addMessage = (message) => {
  const {
    messages,
    name,
  } = getState();
  if (messages.length > 4095) {
    loose();
    console.log(`Buffer overflow on user ${name}`)
    error('PANIC - Buffer overflow');
  }
  return setState({
    messages: [
      ...messages,
      message,
    ],
  });
};

const bprintf = (message) => {
  if (message.length > 255) {
    console.log('Bprintf Short Buffer overflow');
    error('Internal Error in BPRINTF')
  }
  return addMessage(message);
};

export default bprintf;

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
  if ((state.channel === player.location) && isdark(state.channel)) {
    return false;
  }
  return setName(player.playerId)
    .then(true);
};

const pfile = (match, filename) => {
  const content = fListfl(filename);
  return getState().debugMode
    ? `[FILE ${filename} ]\n${content}`
    : content;
};

const pndeaf = (match, message) => !getState().ailDeaf
  ? message
  : '';

const pcansee = (match, name, message) => {
  const player = fpbns(name);
  return (player && seePlayer(player))
    ? message
    : '';
};

const prname = (match, message) => {
  const player = fpbns(name);
  return (player && seeplayer(player))
    ? message
    : 'Someone';
};

const pndark = (match, message) => (!isdark() && ! getState().ailBlind)
  ? message
  : '';

const ppndeaf = (match, message) => {
  if (getState().ailDeaf) {
    return '';
  }
  const player = fpbns(name);
  return (player && seeplayer(player))
    ? message
    : 'Someone';
};

const ppnblind = (match, message) => {
  if (getState().ailBlind) {
    return '';
  }
  const player = fpbns(name);
  return (player && seeplayer(player))
    ? message
    : 'Someone';
};

const pnotkb = isKeyboard => (match, message) => !isKeyboard
  ? message
  : '';

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
        .then(() => dcprnt(messages, logFl, false))
    }
    if (state.snoopDestination) {
      promise
        .then(() => {
          const player = getPlayer(snoopDestination);
          return player && opensnoop(player.name, 'a');
        })
        .then((fln) => Promise.resolve()
          .then(() => dcprnt(messages, fln, false))
          .then(fcloselock)
        )
        .catch(() => {});
    }
    promise
      .then(() => dcprnt(messages, null, true))
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

const setName = (x) => {
  if ((x > 15) && (x != fpbns('riatha')) && (x != fpbns('shazareth'))) {
    return setState({ wdIt: x.name });
  }
  return setState(
    x.sex
      ? {
        wdHer: x.name,
        wdThem: x.name,
      }
      : {
        wdHim: x.name,
        wdThem: x.name,
      }
  )
};
