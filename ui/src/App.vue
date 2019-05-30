<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'BaseApp',
  data () {
    return {
    }
  },
  created () {
    this.$http.interceptors.response.use(undefined, err => {
      const error = err.response
      if (error.status === 401 && error.data.token_type === 'refresh') {
        this.$store.commit('auth/delete_access_token')
        this.$store.commit('auth/delete_refresh_token')
        this.$router.push('/login')
      }

      if (error.status === 401 && error.config && !error.config._isRetryRequest) {
        return this.init_token().then(response => {
          error.config.__isRetryRequest = true
          var new_header = 'Bearer ' + response.data.access_token
          error.config.headers['Authorization'] = new_header
          this.$http.defaults.headers['Authorization'] = new_header
          this.$store.commit('auth/set_access_token', response.data.access_token)
          return this.$http(error.config)
        })
      }
    })
  },
  methods: {
    get_access_token () {
      var refresh_header = 'Bearer ' + this.$store.getters['auth/refresh_token']
      return this.$http.get('refresh', { headers: { Authorization: refresh_header } })
    },
    init_token () {
      if (!this.$store.getters['auth/refreshing_state']) {
        this.$store.commit('auth/set_refreshing_state', this.get_access_token())
        this.$store.getters['auth/refreshing_state'].then(this.reset_refreshing_state, this.reset_refreshing_state)
      }
      return this.$store.getters['auth/refreshing_state']
    },
    reset_refreshing_state () {
      this.$store.commit('auth/set_refreshing_state', false)
    }
  }
}

</script>

<style lang="scss">
body {
  background: linear-gradient(180deg, #343a40 350px, #f4f2f2 350px);
}
</style>