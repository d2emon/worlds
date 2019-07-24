<template>
  <v-container
    fluid
    grid-list-md
  >
    <v-layout row wrap>
      <slot name="before" />

      <v-flex
        v-for="item in cards"
        :key="item.key"
        v-bind="{
          [item.flex.sm]: true,
          [item.flex.lg]: true,
        }"
      >
        <v-card
          :to="item.url"
        >
          <v-card-title
            class="headline"
            v-text="item.title"
          />

          <v-img
            :src="item.image"
            height="200px"
          >
            <!-- v-container
              fill-height
              fluid
              pa-2
            >
              <v-layout fill-height>
                <v-flex xs12 align-end flexbox>
                  <span class="headline white--text" v-text="item.title"></span>
                </v-flex>
              </v-layout>
            </v-container -->
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

      <slot name="after" />
    </v-layout>
  </v-container>
</template>

<script>
export default {
  name: 'ItemsList',
  props: [
    'items',
    'start-offset',
  ],
  data: () => ({
    fullRow: 6,
    row: 6,
    cards: [],
  }),
  watch: {
    items: 'setCards',
  },
  methods: {
    getFlex() {
      const size = Math.floor(Math.random() * (this.row)) + 1;
      this.row = this.row <= size ? this.fullRow : this.row - size;
      return size;
    },
    setCards(items) {
      this.row = this.fullRow - this.startOffset;
      this.cards = items.map((item, key) => {
        const flex = this.getFlex();
        return {
          key,
          ...item,
          flex: {
            sm: `sm${flex * 2}`,
            lg: `lg${flex}`,
          },
          // height: (Math.random() > 0.5) ? '200px' : '400px',
        };
      });
    },
  },
  mounted() {
    this.setCards(this.items);
  },
};
</script>

<style scoped>

</style>
