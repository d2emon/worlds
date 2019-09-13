<template>
  <v-app>
    <v-app-bar>
      <!-- v-app-bar-nav-icon></v-app-bar-nav-icon -->

      <v-toolbar-title class="text-uppercase">
        <router-link to="/">Миры</router-link>
      </v-toolbar-title>

      <div class="flex-grow-1"></div>

      <v-btn
        text
        to="/"
      >
        Миры
      </v-btn>

      <v-btn
        text
        to="/blog"
      >
        Блог
      </v-btn>

      <!-- v-menu
        left
        bottom
      >
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item
            v-for="n in 5"
            :key="n"
            @click="() => {}"
          >
            <v-list-item-title>Option {{ n }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu -->
    </v-app-bar>

    <v-content>
      <v-container>
        <v-layout justify-center>
          <v-flex xs12 sm9>
            <router-view />
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
a {
  text-decoration: none;
}

.wiki blockquote {
  border-left: .25em solid #dfe2e5;
  color: #6a737d;
  padding: 0 1em;
}

.wiki img {
  max-height: 200px;
  max-width: 200px;
}

.v-toolbar a {
  color: #FFFFFF;
}

.v-card__title a {
  color: #000000;
}
</style>
