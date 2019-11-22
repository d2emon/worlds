class Item {
  constructor(itemId) {
    this.itemId = itemId;
    this.name = '';
    this.location = 0;
    this.carryFlag = 0;
    this.flags = {};
    this.data = {};

    this.isWeapon = this.flags[15];
  }
}

class Player {
  constructor(playerId) {
    this.playerId = playerId;
    this.name = '';
    this.strength = 0;
    this.location = 0;
    this.level = 0;

    this.isBot = this.getIsBot();
    this.damage = this.getDamage();
    this.value = this.getValue();
  }

  getIsBot() {
    return this.playerId >= 16;
  }

  getDamage() {
    const damage = {
      18: 6,
      19: 6,
      20: 6,
      21: 6,
      22: 6,
      23: 32,
      24: 8,
      //
      28: 6,
      30: 20,
      31: 14,
      32: 15,
      33: 10,
    };

    return damage[this.playerId] || 10;
  }

  getValue() {
    return this.getIsBot()
      ? (this.level * this.level * 100)
      : (10 * this.getDamage());
  }
}

export const getItem = itemId => new Item(itemId);

export const getPlayer = playerId => new Player(playerId);

export const setPlayer = player => Promise.resolve(null);

export const loadWorld = () => Promise.resolve({
  //
});

export const saveWorld = () => Promise.resolve(null);
