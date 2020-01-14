<template>
  <v-card>
    <v-card-title>
      Мир небесных тел
    </v-card-title>
    <v-container>
      <planet />
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'Astronomy',
  components: {
    Planet: () => import('@/components/volumes/Planet.vue'),
  },
};
</script>

<style scoped>

</style>
