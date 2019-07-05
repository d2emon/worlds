<template>
  <items-list :items="categories" />
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'CategoriesList',
  components: {
    ItemsList: () => import('@/components/ItemsList.vue'),
  },
  computed: {
    ...mapState('categories', [
      'categories',
    ]),
  },
  methods: {
    ...mapActions('categories', [
      'getCategories',
    ]),
  },
  mounted() {
    this.getCategories();
  },
};
</script>

<style scoped>

</style>
