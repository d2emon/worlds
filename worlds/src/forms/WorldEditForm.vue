<template>
  <v-container>
    <v-form
      ref="worldEditForm"
      v-model="valid"
      :lazy-validation="lazy"
    >
      <v-text-field
        v-model="title"
        :rules="titleRules"
        label="Название"
        required
      ></v-text-field>
      <v-text-field
        v-model="image"
        :rules="imageRules"
        label="Изображение"
      ></v-text-field>
      <v-btn
        :disabled="!valid"
        color="success"
        class="mr-4"
        @click="saveWorld"
      >
        Save
      </v-btn>
    </v-form>
  </v-container>
</template>

<script>
export default {
  name: 'WorldEditForm',
  props: [
    'showPortal',
    'world',
    'wiki',
  ],
  data: () => ({
    valid: true,
    lazy: false,

    title: '',
    titleRules: [
      v => !!v || 'Name is required',
    ],
    image: '',
    imageRules: [],
  }),
  methods: {
    setValues(world) {
      this.title = world ? world.title : '';
      this.image = world ? world.image : '';
    },
    saveWorld() {
      if (this.$refs.worldEditForm.validate()) {
        this.$emit('save', {
          slug: this.world && this.world.slug,
          title: this.title,
          image: this.image,
        });
        //
      }
    },
  },
  watch: {
    world(world) {
      this.setValues(world);
    },
  },
  mounted() {
    this.setValues(this.world);
  },
};
</script>

<style scoped>

</style>
