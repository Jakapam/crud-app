import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'

let token = localStorage.getItem("token")
token = token ? `Bearer ${token}` : null

export const axiosRequest = axios.create({
  baseURL: process.env.API_BASE_URL,
  headers:{
    Authorization: token,
    contentType: "Application/Json"
  }
})


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
