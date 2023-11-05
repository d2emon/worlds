<template>
  <v-layout justify-center>
    <v-flex xs12 xl9>
      <world-card
        v-if="world"
        :world="world"
      >
        <v-container>
          <v-layout row wrap>
            <v-flex xs4 md3>
              <world-details
                v-if="world"
                :world="world"
              />
            </v-flex>
            <v-flex xs8 md9>
              <router-view />
            </v-flex>
          </v-layout>
        </v-container>
      </world-card>
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'World',
  components: {
    WorldCard: () => import('@/components/cards/World.vue'),
    WorldDetails: () => import('@/components/WorldDetails.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorld',
    ]),
    fetchAll() {
      const {
        worldId,
      } = this.$route.params;
      this.getWorld(worldId);
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
};
</script>

<style scoped>

</style>
