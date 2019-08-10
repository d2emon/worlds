<template>
  <v-list>
    <v-list-tile
      v-for="item in items"
      :key="`item-${item.item_id}`"
    >
      <v-badge
        v-if="debug"
        :left="true"
        :overlap="false"
      >
        <template v-slot:badge>{{item.item_id}}</template>
        {{item.description}}
      </v-badge>
      <span v-else>{{item.description}}</span>
      <v-chip
        v-if="item.is_destroyed"
        class="ma-2"
        color="red"
        text-color="white"
      >
        Destroyed
      </v-chip>
    </v-list-tile>
  </v-list>
</template>

<script>
export default {
  name: 'GameItems',
  props: [
    'items',
    'debug',
  ],
};
</script>

<style scoped>

</style>
