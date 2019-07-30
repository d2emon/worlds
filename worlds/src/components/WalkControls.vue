<template>
  <v-card>
    <v-card-actions>
      <v-btn
        @click="setBrief(!brief)"
      >
        Brief
      </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import {
  mapState,
  mapMutations,
} from 'vuex';

export default {
  name: 'WalkControls',
  computed: {
    ...mapState('walk', [
      'brief',
      // 'player',
    ]),
  },
  methods: {
    ...mapMutations('walk', ['setBrief']),
  },
}
</script>

<style scoped>

</style>
