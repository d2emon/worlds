<template>
  <v-card>
    <v-card-title>
      <h4>You are carrying:</h4>
    </v-card-title>
    {{inventory}}
  </v-card>
</template>

<script>
import {mapState} from 'vuex';

export default {
  name: 'Inventory',
  computed: {
    ...mapState('walk', ['inventory']),
  },
};
</script>

<style scoped>

</style>
