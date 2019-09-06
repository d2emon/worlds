<template>
  <v-card>
    <v-container>
      <v-row
        v-for="(item, id) in summary"
        :key="`summary-${id}`"
      >
        <template v-if="item.value">
          <v-col>{{item.label}}</v-col>
          <v-col>{{item.value}}</v-col>
        </template>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
export default {
  name: 'WorldSummary',
  props: [
    'world',
  ],
  computed: {
    summary() {
      return Object.keys(this.labels).map(key => ({
        label: this.labels[key],
        value: this.world[key],
      }));
    },
  },
  data: () => ({
    labels: {
      title: 'Название мира',
      createdAt: 'Возникновение',
      author: 'Создатель',
      origin: 'Происхождение',
      media: 'Воплощения',
    },
  }),
};
</script>

<style scoped>

</style>
