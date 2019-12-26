<template>
  <component
    class="wiki"
    v-bind:is="processed"
  ></component>
</template>

<script>
import Vue from 'vue';
import Books from '@/components/Books.vue';

Vue.component('books', Books);

export default {
  name: 'Wiki',
  components: {
    Books,
  },
  computed: {
    processed() {
      const books = this.world && this.world.books;
      console.log(books);
      const html = this.wiki
        .replace(
          '[[books]]',
          '<books :books="books" />',
        );
      return {
        template: `<div>${html}</div>`,
        props: {
          books: {
            type: null,
            default: () => books,
          },
        },
      };
    },
  },
  props: [
    'wiki',
    'world',
  ],
};
</script>

<style>
.wiki h1 {
  font-size: 1.5rem !important;
  font-weight: 400;
  line-height: 2rem;
  letter-spacing: normal !important;
  font-family: "Roboto", sans-serif !important;
}
.wiki h1 {
  margin-bottom: 16px;
}
.wiki h2 {
  margin-bottom: 16px;
}
.wiki h3 {
  margin-bottom: 16px;
}
</style>
