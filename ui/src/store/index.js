import Vue from 'vue'
import Vuex from 'vuex'
import template from '@/store/template'
import auth from '@/store/auth'
import target from '@/store/target'

Vue.use(Vuex)

export const store = new Vuex.Store({
  modules: {
    auth,
    target,
    template
  }
})

export default store
