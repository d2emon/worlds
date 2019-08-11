<template>
  <v-list>
    <v-list-tile
      v-for="item in items"
      :key="`item-${item.item_id}`"
    >
      <v-list-tile-avatar>
        <v-chip
          v-if="item.is_destroyed"
          class="ma-2"
          color="red"
          text-color="white"
        >
          Destroyed
        </v-chip>
        <!-- v-badge
          v-if="debug"
          :left="true"
          :overlap="false"
        >
          <template v-slot:badge>Destroyed</template>
          <v-avatar></v-avatar>
        </v-badge -->
      </v-list-tile-avatar>
      <v-list-tile-content>
        <span v-if="debug">{{item.item_id}}</span>
        {{item.description}}
      </v-list-tile-content>
      <v-list-tile-action>
        <v-btn
          v-if="!flannel"
          @click="take(item.slug)"
        >
          Take
        </v-btn>
        <!-- v-btn @click="console.log(10)">Drop</v-btn -->
      </v-list-tile-action>
    </v-list-tile>
  </v-list>
</template>

<script>
import {mapActions} from 'vuex';

export default {
  name: 'GameItems',
  props: [
    'items',
    'flannel',
    'debug',
  ],
  methods: {
    ...mapActions(
      'walk',
      [
        'take',
      ],
    ),
  },
};
</script>

<style scoped>

</style>
