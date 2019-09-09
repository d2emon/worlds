<template>
  <v-container>
    <wiki
      v-if="wiki !== null"
      :wiki="wiki"
    />
    <page-list
      v-else-if="planet && planet.map && planet.map.wiki"
      :pages="planet.map.wiki"
    />
    <v-card
      v-else
    >
      <v-card-title>
        Планета не найдена!
      </v-card-title>
    </v-card>
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'PlanetMap',
  components: {
    Wiki: () => import('@/components/Wiki.vue'),
    PageList: () => import('@/components/PageList.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'planet',
      'world',
      'wiki',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWiki',
    ]),
    fetchAll() {
      const {
        worldId,
        planetId,
        pageId,
      } = this.$route.params;
      this.getWiki({
        worldId,
        planetId,
        pageId,
        isMap: true,
      });
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
