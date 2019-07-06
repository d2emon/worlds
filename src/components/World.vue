<template>
  <v-container>
    <portal v-model="enteringPortal" />

    <v-card
      v-if="world"
    >
      <v-card-title
        class="headline"
        :to="world.to"
        v-text="world.title"
      />

      <v-img
        :src="world.image"
        height="200px"
      />

      <v-container>
        <!-- Object.keys(world) -->
        <!-- world.title -->
        <!-- world.image -->
        <!-- world.url -->
        <!-- world.text -->
        <!-- world.html -->

        <v-card-text v-html="world.html" />
      </v-container>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>favorite</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>bookmark</v-icon>
        </v-btn>
        <v-btn icon>
          <v-icon>share</v-icon>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'World',
  components: {
    Portal: () => import('@/components/Portal.vue'),
  },
  props: [
    'world',
  ],
  data: () => ({
    enteringPortal: true,
  }),
};
</script>

<style scoped>

</style>
