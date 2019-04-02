import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import axios from 'axios'
import store from './store'
import router from './router'


export const axiosRequest = axios.create({
  baseURL:'http://localhost:5000/api',
  headers:{
    Authorization: "Bearer " + localStorage.getItem("token"),
    contentType: "Application/Json"
  }
})

function verifyToken(token) {
  return axiosRequests.get("/", {
    headers: {
      authorization: token
    }
  })
}

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  store,
  router
}).$mount('#app')
