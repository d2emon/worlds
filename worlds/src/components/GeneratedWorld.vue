<template>
  <world :world="{title: generated ? generated.name : 'Unknown'}">
    <v-container
      v-if="generated"
      fluid
      grid-list-md
    >
      <v-card>
        <v-list>
          <v-list-tile
            v-for="(item, id) in generated.children"
            :key="`item-${id}`"
            :to="`/generated/${item}`"
          >
            <v-list-tile-content>
              <v-list-tile-title v-text="item" />
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-card>
      {{generated}}
    </v-container>
  </world>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'GeneratedWorld',
  components: {
    World: () => import('@/components/World.vue'),
  },
  props: [
    'thing',
  ],
  computed: {
    ...mapState('generate', [
      'generated',
    ]),
  },
  methods: {
    ...mapActions('generate', [
      'getGenerated',
    ]),
    generateChild(child) {
      this.getGenerated(child);
    },
  },
  watch: {
    thing() {
      this.getGenerated(this.thing || 'universe');
    },
  },
  mounted() {
    this.getGenerated(this.thing || 'universe');
  },
};
</script>

<style scoped>

</style>
