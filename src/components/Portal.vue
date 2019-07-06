<template>
  <v-dialog
    v-model="value"
    width="500"
    scrollable
  >
    <v-card>
      <v-card-title
        class="headline grey lighten-2"
        primary-title
      >
        Портал
      </v-card-title>

      <v-img
        src="/images/portal.jpg"
        height="200px"
      >
        <v-container
          fill-height
          fluid
          pa-2
          style="max-height: 200px; overflow: auto;"
        >
          <v-layout fill-height>
            <v-flex xs12 align-end flexbox>
              <v-card-text class="white--text">
                <!-- Описание портала. -->
                <p
                  v-for="(s, id) in portal"
                  :key="id"
                  v-text="s"
                />
              </v-card-text>
            </v-flex>
          </v-layout>
        </v-container>
      </v-img>

      <v-divider></v-divider>

      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          color="primary"
          flat
          @click="$emit('input', false)"
        >
          Войти
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Portal',
  props: [
    'value',
  ],
  computed: {
    ...mapState('worlds', [
      'portal',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getPortal',
    ]),
  },
  mounted() {
    this.getPortal();
  },
};
</script>

<style scoped>

</style>
