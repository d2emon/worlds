<template>
  <v-container>
    <world-summary
      v-if="world"
      class="mb-2"
      :world="world"
    />

    <v-card
      v-if="world.books && world.books.length"
      class="mb-2"
    >
      <books :books="world.books" />
    </v-card>

    <v-card
      v-if="world.pages && world.pages.length"
      class="mb-2"
    >
      <v-list>
        <v-list-item
          v-for="(page, id) in world.pages"
          :key="`page-${id}`"
          :to="page.url"
          :title="page.title"
        >
          <v-list-item-content>
            <v-list-item-title v-text="page.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'WorldDetails',
  components: {
    WorldSummary: () => import('@/components/WorldSummary.vue'),
  },
  props: [
    'world',
  ],
};
</script>

<style scoped>

</style>
