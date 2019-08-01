<template>
  <v-card>
    <v-container>
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

      <v-card-text
        v-if="room.error"
        v-text="room.error"
      />
      <v-card-text
        v-if="!brief"
        v-html="room.html"
      />
      <v-card-text
        v-if="room['5']"
        v-text="room['5']"
      />
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
  props: [
    'room',
  ],
  computed: {
    ...mapState('walk', [
      'brief',
      'player',
    ]),
  },
  methods: {
    ...mapMutations('walk', ['setBrief']),
  },
};
</script>

<style scoped>

</style>
