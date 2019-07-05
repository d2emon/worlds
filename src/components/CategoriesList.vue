<template>
        <v-container
          fluid
          grid-list-md
        >
          <v-layout row wrap>
            <v-flex
              v-for="category in categories"
              :key="category.title"
              v-bind="{ [`xs${getFlex()}`]: true }"
            >
              <v-card
                :to="category.to"
              >
                <v-img
                  :src="category.src"
                  height="200px"
                >
                  <v-container
                    fill-height
                    fluid
                    pa-2
                  >
                    <v-layout fill-height>
                      <v-flex xs12 align-end flexbox>
                        <span class="headline white--text" v-text="category.title"></span>
                      </v-flex>
                    </v-layout>
                  </v-container>
                </v-img>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn icon>
                    <v-icon>favorite</v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon>bookmark</v-icon>
                  </v-btn>
                  <v-btn icon>
                    <v-icon>share</v-icon>
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-flex>
          </v-layout>
        </v-container>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'CategoriesList',
  computed: {
    ...mapState('categories', [
      'categories',
    ]),
  },
  data: () => ({
    sizes: [6], // [6, 12]
  }),
  methods: {
    ...mapActions('categories', [
      'getCategories',
    ]),
    getFlex: function () {
      return this.sizes[Math.floor(Math.random() * this.sizes.length)];
    },
  },
  mounted() {
    this.getCategories();
  }
};
</script>

<style scoped>

</style>
