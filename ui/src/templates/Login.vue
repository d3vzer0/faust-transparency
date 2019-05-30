<template>
  <b-container fluid id="login-container">
    <b-row class="justify-content-md-center top-50">
      <b-col xl="3" lg="4" md="7" sm="8" cols="10" class="center-block">
        <b-card header="Authentication" header-tag="header" id="card-login">
          <!-- <div id="card-login-header">
            <div class="alert alert-danger" v-if="error">{{ error }}</div>
          </div> -->
          <b-form method="post" @submit.prevent="login">
            <b-row class="top-10">
              <b-col cols="12">
                <b-form-input type="text" class="input-field" v-model="username" required placeholder="Username"></b-form-input>
              </b-col>
            </b-row>
            <b-row class="top-10">
              <b-col cols="12">
                <b-form-input type="password" class="input-field" v-model="password" required placeholder="Password"></b-form-input>
              </b-col>
            </b-row>
            <b-row>
              <b-col cols="12" class="top-10">
                <b-button type="submit" variant="primary" class="fullwidth">Submit</b-button>
              </b-col>
            </b-row>
          </b-form>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
import VueJwtDecode from 'vue-jwt-decode'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      error: false
    };
  },
  methods: {
    login () {
      this.$http
        .post("login", { username: this.username, password: this.password })
        .then(response => this.login_success(response))
        .catch(response => this.login_failed(response))
    },
    login_success (response) {
      if (!response.data.access_token) {
        this.login_failed()
        return
      }

      this.$store.commit('auth/set_claims', response.data.access_token)
      this.$store.commit('auth/set_access_token', response.data.access_token)
      this.$store.commit('auth/set_refresh_token', response.data.refresh_token)
      this.$router.push('/home')
    },
    login_failed (response) {
      this.error = 'Unable to login'
      this.$store.commit('auth/delete_access_token')
      this.$store.commit('auth/delete_refresh_token')
    }
  }
}
</script>

<style lang="scss" scoped>
@import url('https://fonts.googleapis.com/css?family=Open+Sans');
@import '@/assets/style.scss';

#header-image {
  width: 100%;
}

// * {box-sizing: border-box;}

#login-container {
  max-width: 80%;
  min-height: 100vh;

}
#card-login {
  .input-container {
    display: flex;
    width: 100%;
    margin-bottom: 15px;
  }
  .icon {
    padding: 10px;
    background: #9d3a3a;
    color: white;
    min-width: 50px;
    text-align: center;
  }
  .input-field {
    box-sizing:border-box;
    border-radius: 0px;
    width: 100%;
    padding: 10px;
    outline: none;
    height: 100%;
  }
  .input-field:focus {
    border: 2px solid #9d3a3a;
  }
  #sidebar-header-image {
    width: 80%;
  }
}

</style>