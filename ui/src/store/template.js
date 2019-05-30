export default {
  namespaced: true,
  state: {
    template: 'login-template'
  },
  mutations: {
    change_template (state, payload) {
      state.template = payload
    }
  },
  getters: {
    current_template (state) {
      return state.template
    }
  }
}
