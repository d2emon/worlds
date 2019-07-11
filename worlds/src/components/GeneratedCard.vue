<template>
  <v-card
    to="/generated"
  >
    <portal v-model="enteringPortal" />

    <v-card-title class="headline">Генерируемый мир</v-card-title>

    <v-img
      :src="config.worldImage"
      height="200px"
    >
      <!-- v-btn
        color="primary"
        dark
        @click.stop="enterPortal"
      >
        Случайный Мир
      </v-btn -->
    </v-img>
  </v-card>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'GeneratedWorld',
  components: {
    Portal: () => import('@/components/Portal.vue'),
  },
  computed: {
    ...mapState(['config']),
  },
  data: () => ({
    enteringPortal: false,
  }),
  methods: {
    ...mapActions('worlds', [
      'getPortal',
    ]),
    enterPortal() {
      this.getPortal();
      this.enteringPortal = true;
    },
  },
};
</script>

<style scoped>

</style>
