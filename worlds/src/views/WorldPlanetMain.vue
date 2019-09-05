<template>
  <planet
    :planet="planet"
  >
    <v-layout row wrap
      v-if="world.pages"
    >
      <v-flex xs4>
        <v-container>
          <v-card>
            <v-list>
                  <v-list-tile
                    v-for="(page, id) in world.pages"
                    :key="`page-${id}`"
                    :to="`/wiki/${page.url}`"
                    :title="page.filename"
                  >
                    <v-list-tile-content>
                      <v-list-tile-title v-text="page.filename" />
                    </v-list-tile-content>
                  </v-list-tile>
            </v-list>
          </v-card>
        </v-container>
      </v-flex>
      <v-flex xs8>
        <slot />
      </v-flex>
    </v-layout>
  </planet>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'WorldPlanetMain',
  components: {
    Planet: () => import('@/components/Planet.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'world',
      'planet',
    ]),
  },
};
</script>

<style scoped>

</style>
