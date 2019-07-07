<template>
  <v-container>
    <v-card>
      <v-card-title class="headline">
        Миры
      </v-card-title>

      <v-container>
        <portal v-model="enteringPortal" />

        <items-list
          :items="worlds"
          :start-offset="2"
        >
          <template v-slot:before>
          <v-flex sm4>
            <v-card>
              <v-card-title class="headline">Случайный мир</v-card-title>

              <v-img
                src="/media/images/worlds/portal.jpg"
                height="200px"
              >
                <v-btn
                  color="primary"
                  dark
                  @click.stop="enterPortal"
                >
                  Случайный Мир
                </v-btn>
              </v-img>

              <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn icon>
                  <v-icon>favorite</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>bookmark</v-icon>
                </v-btn>
                <v-btn icon>
                  <v-icon>share</v-icon>
                </v-btn>
              </v-card-actions>
             </v-card>
            </v-flex>
          </template>
        </items-list>
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
