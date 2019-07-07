<template>
  <v-container>
    <v-card>
      <v-card-title class="headline">
        Миры
      </v-card-title>

      <v-container>
        <v-btn
          color="primary"
          dark
          @click.stop="enterPortal"
        >
          Случайный Мир
        </v-btn>

        <portal v-model="enteringPortal" />

        <items-list :items="worlds" />
      </v-container>
    </v-card>
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
  /*
  computed: {
    ...mapState('worlds', [
      'worlds',
    ]),
  },
  */
  props: [
    'worlds',
  ],
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
