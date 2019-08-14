<template>
  <v-layout justify-center wrap>
    <v-flex xs12>
      <v-container>
        <h4>{{progname}}</h4>
      </v-container>
    </v-flex>
    <v-flex xs12 sm3>
      <v-container>
        <walk-controls />
      </v-container>
    </v-flex>
    <v-flex xs12 sm6>
      <v-container>
        <room />
      </v-container>
    </v-flex>
    <v-flex xs12 sm3>
      <v-container>
        <inventory />
        {{characters}}
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Walk',
  components: {
    WalkControls: () => import('@/components/WalkControls.vue'),
    Room: () => import('@/components/Room.vue'),
    Inventory: () => import('@/components/Inventory.vue'),
  },
  computed: {
    ...mapState('walk', [
      'progname',
      'characters',
    ]),
  },
  methods: {
    ...mapActions('walk', [
      'getRoom',
    ]),
    fetchAll() {
      this.getRoom();
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
}
</script>

<style scoped>

</style>
