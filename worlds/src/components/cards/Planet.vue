<template>
  <v-container>
    <template
      v-if="planet"
    >
      <v-card-title>
        <h2>
          <router-link
            :to="planet.url"
            v-text="planet.name"
          ></router-link>
        </h2>
      </v-card-title>

      <slot />
    </template>
  </v-container>
</template>

<script>
export default {
  name: 'Planet',
  props: [
    'planet',
  ],
  data: () => ({}),
};
</script>
