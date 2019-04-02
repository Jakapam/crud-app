import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'

export const axiosRequest = axios.create({
  baseURL:'http://localhost:5000/api',
  headers:{
    Authorization: "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTQxODEyNzgsIm5iZiI6MTU1NDE4MTI3OCwianRpIjoiMzQyYTFjMTgtZDYwOS00NjllLWI5NzYtYzZmZTkyYmE1NGIxIiwiaWRlbnRpdHkiOiJqdXN0aW4iLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.OlfhTVmJQ3_hUehCGqmbp-5S-E44efWd33gTU7qORbg",
    contentType: "Application/Json"
  }
})

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
