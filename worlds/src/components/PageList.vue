<template>
  <v-list>
    <v-list-item
      v-for="(page, id) in pages"
      :key="`page-${id}`"
      :to="page.url"
      :title="page.title"
    >
      <v-list-item-content
        v-text="page.title"
      ></v-list-item-content>
    </v-list-item>
  </v-list>
</template>

<script>
export default {
  name: 'PageList',
  props: [
    'pages',
  ],
};
</script>

<style scoped>

</style>
