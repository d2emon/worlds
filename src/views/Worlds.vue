<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <worlds-list />
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'Worlds',
  components: {
    WorldsList: () => import('@/components/Worlds.vue'),
  },
};
</script>

<style scoped>

</style>
