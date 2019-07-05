<template>
  <v-layout justify-center>
    <v-flex xs12 sm6>
      <!-- v-toolbar color="indigo" dark>
        <v-toolbar-side-icon></v-toolbar-side-icon>
        <v-toolbar-title>Миры</v-toolbar-title>
        <v-spacer></v-spacer>
        <v-btn icon>
          <v-icon>search</v-icon>
        </v-btn>
      </v-toolbar -->

      <!-- v-card>
        <categories-list />
      </v-card -->

      <categories-list />
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'Categories',
  components: {
    CategoriesList: () => import('@/components/CategoriesList.vue'),
  },
};
</script>

<style scoped>

</style>
