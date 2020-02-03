<template>
  <v-layout justify-center wrap>
    <v-flex xs12>
      <v-container>
        <h4>{{progname}}</h4>
      </v-container>
    </v-flex>
    <v-flex xs12 sm3>
      <v-container>
        <walk-controls />
      </v-container>
    </v-flex>
    <v-flex xs12 sm6>
      <v-container>
        <room />
      </v-container>
    </v-flex>
    <v-flex xs12 sm3>
      <v-container>
        <inventory class="mb-2" />
        <v-card
          v-if="characters && characters.players && characters.players.length"
          class="mb-2"
        >
          <v-card-title>
            Игроки:
          </v-card-title>
          <v-list>
            <v-list-tile
              v-for="character in characters.players"
              :key="character.character_id"
            >
              <v-list-tile-avatar>
                <v-chip v-if="character.invisible">Invisible</v-chip>
              </v-list-tile-avatar>
              <v-list-tile-content>
                {{character.name}} {{character.level}}
                <span v-if="character.absent">[Absent From Reality]</span>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
        <v-card
          v-if="characters && characters.mobiles && characters.mobiles.length"
          class="mb-2"
        >
          <v-card-title>
            Существа:
          </v-card-title>
          <v-list>
            <v-list-tile
              v-for="character in characters.mobiles"
              :key="character.character_id"
            >
              <v-list-tile-avatar>
                <v-chip v-if="character.invisible">Invisible</v-chip>
              </v-list-tile-avatar>
              <v-list-tile-content>
                {{character.name}} {{character.level}}
                <span v-if="character.absent">[Absent From Reality]</span>
              </v-list-tile-content>
            </v-list-tile>
          </v-list>
        </v-card>
      </v-container>
    </v-flex>
  </v-layout>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Walk',
  components: {
    WalkControls: () => import('@/components/walk/WalkControls.vue'),
    Room: () => import('@/components/Room.vue'),
    Inventory: () => import('@/components/Inventory.vue'),
  },
  computed: {
    ...mapState('walk', [
      'progname',
      'characters',
    ]),
  },
  methods: {
    ...mapActions('walk', [
      'getRoom',
    ]),
    fetchAll() {
      this.getRoom();
    },
  },
  watch: {
    $route() { this.fetchAll(); },
  },
  mounted() { this.fetchAll(); },
}
</script>

<style scoped>

</style>
