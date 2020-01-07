<template>
  <v-card>
    <v-card-title>
      Земля
    </v-card-title>
    <v-container>
      <geology />
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'Planet',
  components: {
    Geology: () => import('@/components/volumes/Geology.vue'),
  },
};
</script>

<style scoped>

</style>
