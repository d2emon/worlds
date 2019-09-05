<template>
  <div
    class="wiki"
    v-html="wiki"
  ></div>
</template>

<script>
export default {
  name: 'Wiki',
  props: [
    'wiki',
  ],
};
</script>

<style scoped>

</style>
