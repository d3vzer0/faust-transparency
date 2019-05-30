import Vue from 'vue'
import App from './App.vue'
import axios from './api'
import './plugins/bootstrap-vue'
import router from './router'
import { store } from '@/store'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'

import { faPlus, faSearch, faExclamationTriangle, faCertificate, faFish, faUserSecret, faUnlock, faUser, faHeart, faTextWidth, faPercent, faCog, faBullseye, faCameraRetro, faPercentage } from '@fortawesome/free-solid-svg-icons'

library.add(
  faExclamationTriangle,
  faCertificate,
  faFish,
  faUserSecret,
  faHeart,
  faTextWidth,
  faPercent,
  faCog,
  faBullseye,
  faCameraRetro,
  faPercentage,
  faUser,
  faSearch,
  faUnlock,
  faPlus,
)

Vue.component('font-awesome-icon', FontAwesomeIcon)
Vue.config.productionTip = false

new Vue({
  store,
  router,
  axios,
  render: h => h(App)
}).$mount('#app')
