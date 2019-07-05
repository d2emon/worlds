<template>
  <v-container>
    <v-btn
      color="primary"
      dark
      @click.stop="enteringPortal = true"
    >
      Случайный Мир
    </v-btn>

    <portal v-model="enteringPortal" />

    <items-list :items="worlds" />
  </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Worlds',
  components: {
    Portal: () => import('@/components/Portal.vue'),
    ItemsList: () => import('@/components/ItemsList.vue'),
  },
  computed: {
    ...mapState('worlds', [
      'worlds',
    ]),
  },
  data: () => ({
    enteringPortal: false,
  }),
  methods: {
    ...mapActions('worlds', [
      'getWorlds',
    ]),
  },
  mounted() {
    this.getWorlds();
  },
};
</script>

<style scoped>

</style>
