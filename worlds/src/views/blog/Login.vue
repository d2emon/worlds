<template>
  <v-card
    flat
    dark
  >
    <v-row justify="center">
      <v-col md="4">
        <v-card light>
          <v-card-title>Sign In</v-card-title>
          <v-container>
            <v-form
              ref="loginForm"
              v-model="valid"
            >
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                :error-messages="loginErrors['username']"
                label="Username"
              ></v-text-field>
              <v-text-field
                type="password"
                v-model="password"
                :rules="passwordRules"
                :error-messages="loginErrors['password']"
                label="Password"
              ></v-text-field>
              <v-checkbox
                v-model="rememberMe"
                :rules="[v => true]"
                :error-messages="loginErrors['remember_me']"
                label="Remember Me"
              ></v-checkbox>
              <v-btn
                :disabled="!valid"
                color="success"
                class="mr-4"
                @click="validate"
              >
                Sign In
              </v-btn>
            </v-form>
          </v-container>
        </v-card>
      </v-col>
    </v-row>
  </v-card>
</template>

<script>
import {
  mapState,
  mapActions,
} from 'vuex';

export default {
  name: 'Login',
  data: () => ({
    valid: true,

    username: '',
    password: '',
    rememberMe: false,

    usernameRules: [
      v => !!v || 'Username is required',
      v => (v && v.length <= 32) || 'Name must be less than 32 characters',
    ],
    passwordRules: [
      v => !!v || 'Password is required',
      v => (v && v.length <= 32) || 'Password must be less than 32 characters',
    ],
  }),
  computed: {
    ...mapState('blog', ['errors']),
    loginErrors() { return this.errors ? (this.errors.login || {}) : {}; },
  },
  methods: {
    ...mapActions('blog', ['doLogin']),
    validate() {
      if (this.$refs.loginForm.validate()) {
        this.doLogin({
          username: this.username,
          password: this.password,
          remember_me: this.rememberMe,
        })
          .then((result) => {
            if (result) {
              this.$router.push('/blog/');
            }
          });
      }
    },
  },
};
</script>

<style scoped>

</style>
