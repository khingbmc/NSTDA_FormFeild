// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import VueMaterial from 'vue-material'
import 'vue-material/dist/vue-material.min.css'
import 'vue-material/dist/theme/default.css'

import { mdbFooter, mdbContainer, mdbRow, mdbCol, mdbvue } from 'mdbvue'

import VueAxios from 'vue-axios'
import axios from 'axios'


axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*'

Vue.use(VueMaterial)
Vue.use(VueAxios, axios)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
