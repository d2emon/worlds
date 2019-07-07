<template>
  <v-container>
    <v-card>
      <v-card-title class="headline">
        Миры
      </v-card-title>

      <v-container>
        <items-list
          :items="worlds"
          :start-offset="2"
        >
          <template v-slot:before>
            <v-flex sm4>
              <random-world />
            </v-flex>
          </template>
        </items-list>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'Worlds',
  components: {
    RandomWorld: () => import('@/components/RandomWorld.vue'),
    ItemsList: () => import('@/components/ItemsList.vue'),
  },
  props: [
    'worlds',
  ],
};
</script>

<style scoped>

</style>
