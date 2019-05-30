export default {
    namespaced: true,
    state: {
      domain: ''
    },
    mutations: {
      update_domain (state, payload) {
        state.domain = payload
      }
    },
    getters: {
      domain (state) {
        return state.domain
      }
    }
  }
  