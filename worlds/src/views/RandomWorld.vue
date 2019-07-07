<template>
  <div>Идет перенаправление...</div>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'RandomWorld',
  computed: {
    ...mapState('worlds', [
      'worlds',
    ]),
  },
  methods: {
    ...mapActions('worlds', [
      'getWorlds',
    ]),
    selectRandom() {
      if (!this.worlds) return {};
      return this.worlds[Math.floor(Math.random() * this.worlds.length)]
    },
  },
  mounted() {
    this.getWorlds()
      .then(this.selectRandom)
      .then(({ url }) => this.$router.replace(url));
  },
};
</script>

<style scoped>

</style>
