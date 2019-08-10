<template>
  <v-card
    :dark="room && room.is_dark"
  >
    <v-container v-if="room">
      <template v-if="player.is_wizard">
        <v-card-title>
          <span v-if="room.name">{{room.name}}</span>
          <span v-if="player.is_god">[ {{room.room_id}} ]</span>
        </v-card-title>
        <v-card-title v-if="room.death">
          &gt;DEATH ROOM&lt;
        </v-card-title>
      </template>
      <v-card-title
        class="headline"
        v-text="room.title"
      />

      <v-layout row wrap>
        <v-flex sm8>
          <v-alert
            v-if="room.error"
            type="error"
            v-text="room.error"
          />
          <v-card-text
            v-if="!brief"
            v-html="room.html"
          />
          <v-layout row wrap>
            <v-flex md6>
              <v-list>
                <v-list-tile
                  v-for="item in room.flannel"
                  :key="`item-${item.item_id}`"
                >
                  <span v-if="item.destroyed">--</span>
                  <span v-if="debugMode">{ {{item.item_id}} }</span>
                  {{item.text}}
                </v-list-tile>
                <v-list-tile v-if="room.weather">{{room.weather}}</v-list-tile>
                <v-list-tile
                  v-for="item in room.items"
                  :key="`item-${item.item_id}`"
                >
                  <span v-if="item.destroyed">--</span>
                  <span v-if="debugMode">{ {{item.item_id}} }</span>
                  {{item.text}}
                </v-list-tile>
              </v-list>
            </v-flex>
            <v-flex md6>
              <div v-if="room.characters">
                <div
                  v-for="character in room.characters"
                  :key="`char-${character.character_id}`"
                >
                  <div>
                    {{character.name}}
                    <span v-if="debugMode">{ {{character.character_id}} }</span>
                    {{character.level}}
                     is here carrying
                  </div>
                  <v-list v-if="character.items">
                    <v-list-tile
                      v-for="(item, item_id) in character.items"
                      :key="`char-${character.character_id}-item-${item_id}`"
                    >
                      {{item}}
                    </v-list-tile>
                  </v-list>
                </div>
              </div>
            </v-flex>
          </v-layout>
        </v-flex>
        <v-flex sm4>
          <v-alert
            v-for="(message, messageId) in reversed"
            :key="`message-${messageId}`"
            v-model="showMessages"
            type="info"
          >
            {{message}}
          </v-alert>
        </v-flex>
      </v-layout>
    </v-container>
  </v-card>
</template>

<script>
import {
  mapState,
  mapMutations,
} from 'vuex';

export default {
  name: 'Room',
  computed: {
    ...mapState('walk', [
      'brief',
      'debugMode',
      'player',
      'room',
      'messages',
    ]),
    reversed() { return this.messages.reverse(); }
  },
  data: () => ({
    showMessages: true,
  }),
  methods: {
    ...mapMutations('walk', ['setBrief']),
  },
};
</script>

<style scoped>

</style>
