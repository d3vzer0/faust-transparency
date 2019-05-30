import VueJwtDecode from 'vue-jwt-decode'

export default {
  namespaced: true,
  state: {
    access_token: localStorage.access_token || false,
    refresh_token: localStorage.refresh_token || false,
    username: '',
    role: '',
    refreshing_state: ''
  },
  mutations: {
    set_claims (state, payload) {
      state.username = VueJwtDecode.decode(payload).identity
      state.role = VueJwtDecode.decode(payload).user_claims.role
    },
    set_access_token (state, token) {
      localStorage.access_token = token
      state.access_token = token
    },
    set_refresh_token (state, token) {
      localStorage.refresh_token = token
      state.refresh_token = token
    },
    delete_refresh_token (state) {
      state.refresh_token = false
      delete localStorage.refresh_token
    },
    delete_access_token (state) {
      state.access_token = false
      delete localStorage.access_token
    },
    set_refreshing_state (state, value) {
      state.refreshing_state = value
    }
  },
  getters: {
    claims (state) {
      return { role: state.role, username: state.username }
    },
    refreshing_state (state) {
      return state.refreshing_state
    },
    access_token (state) {
      return state.access_token
    },
    refresh_token (state) {
      return state.refresh_token
    },
    expiry_state (state) {
      return {
        access: VueJwtDecode.decode(state.access_token).exp,
        refresh: VueJwtDecode.decode(state.refresh_token).exp
      }
    }
  }
}
