<template>
  <v-container>
    <portal
      v-if="showPortal"
      v-model="enteringPortal"
    />

    <slot />

    <!-- Object.keys(world) -->
    <!-- world.title -->
    <!-- world.image -->
    <!-- world.url -->
    <!-- world.text -->
    <!-- world.html -->

    <v-card-text
      v-if="wiki"
    >
      <wiki
        :wiki="wiki"
        :world="world"
      />
    </v-card-text>

    <v-card-text
      v-else-if="world.html"
    >
      <wiki
        :wiki="world.html"
        :world="world"
      />
    </v-card-text>

    <v-container v-else>
      <page-list
        v-if="world.pages"
        :pages="world.pages"
      />

      <v-layout
        v-if="world.data && world.data.cards"
        row
        wrap
      >
        <v-flex
          sm4
          class="pa-1"
          v-for="(card, id) in world.data.cards"
          :key="`card-${id}`"
        >
          <v-card>
            <a
              :href="card.image"
              target="_blank"
            >
              <v-img
                v-if="card.image"
                :src="card.image"
              />
            </a>

            <v-card-title>
              <h3 class="headline" v-text="card.title"></h3>
              <div v-text="card.text"></div>
            </v-card-title>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
  </v-container>
</template>

<script>
import wikipedia from '@/assets/wiki/wiki.png';
import lurkmore from '@/assets/wiki/lurk.png';
import posmotreli from '@/assets/wiki/posmotreli.png';

export default {
  name: 'World',
  components: {
    Books: () => import('@/components/Books.vue'),
    PageList: () => import('@/components/PageList.vue'),
    Portal: () => import('@/components/Portal.vue'),
    WorldSummary: () => import('@/components/WorldSummary.vue'),
    Wiki: () => import('@/components/Wiki.vue'),
  },
  props: [
    'showPortal',
    'world',
    'wiki',
  ],
  data: () => ({
    enteringPortal: true,
    wikiLogo: {
      wikipedia,
      lurkmore,
      posmotreli,
    },
  }),
};
</script>

<style scoped>

</style>
