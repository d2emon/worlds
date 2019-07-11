<template>
  <v-layout justify-center>
    <v-flex xs12 sm9>
      <generated-world />
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  name: 'Geneverse',
  components: {
    GeneratedWorld: () => import('@/components/GeneratedWorld.vue'),
  },
};
</script>

<style scoped>

</style>
