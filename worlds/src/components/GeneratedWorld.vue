<template>
  <world :world="{title: generated ? generated.name : 'Unknown'}">
    {{generated}}
    <h1>{{generated.name}}</h1>
    <v-container
      v-if="generated"
      fluid
      grid-list-md
    >
      <v-layout row wrap>
        <v-flex
          v-for="(item, id) in generated.children"
          :key="id"
          sm3
        >
          <v-card
            @click="generateChild(item)"
          >
            <v-card-title
              class="headline"
              v-text="item"
            />

            {{item}}

          </v-card>
        </v-flex>
      </v-layout>
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
  mounted() {
    this.getGenerated('universe');
  },
};
</script>

<style scoped>

</style>
