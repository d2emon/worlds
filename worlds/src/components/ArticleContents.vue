<template>
  <div>
    <router-link
      :to="url"
      v-text="title"
    ></router-link>
    <ul
       v-if="children"
    >
      <li
        v-for="child in children"
        :key="child.title"
      >
        <article-contents
          v-if="child"
          :title="child.title"
          :url="child.url"
          :children="child.children"
        />
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'ArticleContents',
  props: [
    'children',
    'title',
    'url',
  ]
};
</script>

<style scoped>

</style>
