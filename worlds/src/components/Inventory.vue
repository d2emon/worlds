<template>
  <v-card>
    <v-card-title>
      <h4>You are carrying:</h4>
    </v-card-title>
    <v-list v-if="inventory && inventory.length">
      <v-list-tile
        v-for="item in inventory"
        :key="`inventory-${item.item_id}`"
      >
        <v-list-tile-avatar>
          <v-chip v-if="item.is_destroyed">Destroyed</v-chip>
        </v-list-tile-avatar>
        <v-list-tile-content>
          <span v-if="debugMode">{{item.item_id}}</span>
          {{item.name}}
          <span v-if="item.is_worn">&lt;worn&gt;</span>
        </v-list-tile-content>
        <v-list-tile-action>
          <!-- v-btn @click="console.log(10)">Drop</v-btn -->
        </v-list-tile-action>
      </v-list-tile>
    </v-list>
    <v-container v-else>
      Nothing!
    </v-container>
  </v-card>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Inventory',
  computed: {
    ...mapState('walk', [
      'inventory',
      'debugMode',
    ]),
  },
};
</script>

<style scoped>

</style>
