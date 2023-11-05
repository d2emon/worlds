<template>
  <v-card>
    <v-card-title>
      Зарубежные страны
    </v-card-title>
    <v-container>
      <country />
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'Countries',
  components: {
    Country: () => import('@/components/volumes/Country.vue'),
  },
};
</script>

<style scoped>

</style>
