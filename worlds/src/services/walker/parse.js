import {
  sendWizardMessage,
} from './events';
import {
  setPlayer,
} from './world';
import {
  bprintf,
  _p,
  _f,
} from './messages';

const levelof = () => 0;
const disle3 = (level, sex) => '';

const Global = {
  GWIZ: 'GWIZ',

  name: '',
  sentence: '',
  position: 0,

  wdIt: '',
  wdThem: '',
  wdHim: '',
  wdHer: '',
  wdThere: '',

  parsed: [],
  wordId: 0,
};

const pronouns = {
  it: Global.wdIt,
  them: Global.wdThem,
  him: Global.wdHim,
  her: Global.wdHer,
  me: Global.name,
  myself: Global.name,
  there: Global.wdThere,
};

const parse = (sentence) => {
  Global.sentence = sentence;
  Global.position = 0;

  Global.parsed = sentence.split(' ');
};

export const nextWord = () => {
  let result = '';

  while ((Global.wordId < Global.parsed.length - 1) && !result) {
    Global.wordId += 1;
    result = Global.parsed[Global.wordId].toLowerCase();
  }
  if (pronouns[result] !== undefined) {
    result = pronouns[result];
  }
  return result;
};


export const updatePlayer = () => {
  if (!Global.iSetup) return Promise.resolve();

  const level = levelof(Global.score);
  if (level !== Global.level) {
    Global.level = level;
    console.log(`${Global.name} to level ${level}`);
    bprintf(`You are now ${Global.name} ${disle3(level, Global.sex)}`);
    sendWizardMessage(`${_p(Global.name)} is now level ${Global.level}`);
    if (level === 10) {
      bprintf(_f(Global.GWIZ));
    }
  }
  if (Global.strength > 30 + 10 * Global.level) {
    Global.strength = 30 + 10 * Global.level;
  }
  return setPlayer({
    playerId: Global.playerId,
    strength: Global.strength,
    sex: Global.sex,
    weapon: Global.weapon,
  });
};
