<template>
  <div>
    <h3>{{ category.title }}</h3>
    <ul
      v-if="category.books"
    >
      <li
        v-for="book in category.books"
        :key="book['book_id']"
      >
        <span>{{ book['book_id'] }}</span> {{ book.title }}
      </li>
    </ul>
    <ul
      v-if="category.categories"
    >
      <li
        v-for="(subcategory, subcategoryId) in category.categories"
        :key="`${categoryId}-${subcategoryId}`"
      >
        <book-category
          :category-id="`${categoryId}-${subcategoryId}`"
          :category="subcategory"
        />
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'BookCategory',
  props: [
    'categoryId',
    'category',
  ],
};
</script>

<style scoped>

</style>
