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

<style>
.wiki h1 {
  font-size: 1.5rem !important;
  font-weight: 400;
  line-height: 2rem;
  letter-spacing: normal !important;
  font-family: "Roboto", sans-serif !important;
}
</style>
