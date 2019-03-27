import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

export const axiosRequest = axios.create({
  baseURL:'http://localhost:5000/'
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
