import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'


export const axiosRequest = axios.create({
  baseURL: process.env.API_BASE_URL,
  headers:{
    Authorization: "Bearer " + localStorage.getItem("token"),
    contentType: "Application/Json"
  }
})


Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
