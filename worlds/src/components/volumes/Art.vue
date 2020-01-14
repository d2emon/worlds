<template>
  <v-card>
    <v-card-title>
      Искусство
    </v-card-title>
    <v-container>
      <literature />
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'Art',
  components: {
    Literature: () => import('@/components/volumes/Literature.vue'),
  },
};
</script>

<style scoped>

</style>
