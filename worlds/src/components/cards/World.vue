<template>
  <v-card>
    <template
      v-if="world"
    >
      <v-img
        v-if="world.image"
        :src="world.image"
        height="200px"
      />

      <v-card-actions>
        <v-btn
          to="/"
          icon
        >
          <v-icon>mdi-view-module</v-icon>
        </v-btn>
        <v-btn
          to="/random-world"
          icon
        >
          <v-icon>mdi-gesture</v-icon>
        </v-btn>

        <v-spacer />

        <template v-if="world && world.wiki">
          <v-btn
            v-for="(href, k) in world.wiki"
            :key="k"
            :href="href"
            target="_blank"
            :icon="!!wikiLogo[k]"
            text
          >
            <v-avatar
              v-if="wikiLogo[k]"
              :size="32"
            >
              <img
                v-if="wikiLogo[k]"
                :src="wikiLogo[k]"
                :alt="k"
              />
            </v-avatar>
            <span v-else>
              {{k}}
            </span>
          </v-btn>
        </template>
      </v-card-actions>
    </template>

    <v-container>
      <v-card-title
        class="headline"
      >
        <router-link
          v-if="world"
          :to="world.url"
          v-text="world.title"
        />
      </v-card-title>

      <slot />
    </v-container>
  </v-card>
</template>

<script>
import wikipedia from '@/assets/wiki/wiki.png';
import lurkmore from '@/assets/wiki/lurk.png';
import posmotreli from '@/assets/wiki/posmotreli.png';

export default {
  name: 'WorldCard',
  props: [
    'world',
  ],
  data: () => ({
    wikiLogo: {
      wikipedia,
      lurkmore,
      posmotreli,
    },
  }),
};
</script>
