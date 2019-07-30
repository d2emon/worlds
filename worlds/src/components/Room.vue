<template>
  <v-card>
    <v-card-title
      class="headline"
    >
      <div
        v-if="player.is_wizard && room.death"
      >
        &lt;DEATH ROOM&gt;
      </div>
      {{room.title}}
    </v-card-title>

    <v-container>
      <v-card-text
        v-if="room.error"
        v-text="room.error"
      />
      <v-card-text
        v-if="!brief"
        v-html="room.html"
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
}
</script>

<style scoped>

</style>
