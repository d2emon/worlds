<template>
  <v-container>
    <v-layout
      row
      wrap
    >
      <v-flex xs6>
        <v-container>
          <world-edit-form
            v-if="world"
            :world="world"
            :wiki="wiki"
            @save="setWorld"
          />
        </v-container>
      </v-flex>
      <v-flex xs6>
        <v-container>
          <v-card>
            <world-volumes />
          </v-card>
        </v-container>
      </v-flex>
    </v-layout>
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
    WorldEditForm: () => import('@/forms/WorldEditForm.vue'),
    WorldVolumes: () => import('@/components/WorldVolumes.vue'),
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
