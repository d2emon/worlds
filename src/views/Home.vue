<template>
  <hello-world />
</template>

<script>
export default {
  components: {
    HelloWorld: () => import('@/components/HelloWorld.vue'),
  },
};
</script>
