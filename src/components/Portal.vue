<template>
  <v-dialog
    v-model="value"
    width="500"
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
        >
          <v-layout fill-height>
            <v-flex xs12 align-end flexbox>
              <div class="white--text">
                Описание портала.
              </div>
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
export default {
  name: 'Portal',
  props: [
    'value',
  ],
  data: () => ({
    show: false,
  }),
};
</script>

<style scoped>

</style>
