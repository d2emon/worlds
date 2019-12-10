<template>
  <v-card>
    <v-card-title>
      Материалы
    </v-card-title>
    <v-card-text>
      <ul>
        <li
          v-for="(category, categoryId) in books"
          :key="categoryId"
        >
          <book-category
            :category-id="categoryId"
            :category="category"
          />
        </li>
      </ul>
    </v-card-text>
  </v-card>
</template>

<script>
export default {
  name: 'Books',
  components: {
    BookCategory: () => import('@/components/BookCategory.vue'),
  },
  props: [
    'books',
  ],
};
</script>
