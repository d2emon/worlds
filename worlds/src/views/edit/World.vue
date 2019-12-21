<template>
  <v-container>
    <world-edit-form
      v-if="world"
      :world="world"
      :wiki="wiki"
      @save="setWorld"
    />
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'EditWorld',
  components: {
    WorldEditForm: () => import('@/components/WorldEditForm.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
      'wiki',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWiki',
      'setWorld',
    ]),
    fetchAll() {
      const {
        worldId,
        pageId,
      } = this.$route.params;
      this.getWiki({
        worldId,
        pageId,
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
