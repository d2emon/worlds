<template>
  <v-row justify="center">
    <v-col md="4">
      <v-card>
        <v-card-title>Sign In</v-card-title>
        <v-container>
          <v-form
            ref="loginForm"
            v-model="valid"
          >
            <v-text-field
              v-model="username"
              :rules="usernameRules"
              label="Username"
            ></v-text-field>
            <v-text-field
              v-model="password"
              :rules="passwordRules"
              label="Password"
            ></v-text-field>
            <v-checkbox
              v-model="rememberMe"
              :rules="[v => true]"
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
</template>

<script>
import { mapActions } from 'vuex';

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
  methods: {
    ...mapActions('blog', ['doLogin']),
    validate() {
      if (this.$refs.loginForm.validate()) {
        console.log('validate');
        this.doLogin({
          username: this.username,
          password: this.password,
          rememberMe: this.rememberMe,
        });
      }
    }
  },
};
</script>

<style scoped>

</style>
