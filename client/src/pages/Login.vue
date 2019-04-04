<template>
  <div>
      LOGIN
      <form @submit.prevent="handleSubmit">
        <input v-model="username" placeholder="username">
        <input v-model="password" placeholder="password">
        <input type="submit" value="login"/>
      </form>
  </div>
</template>

<script>
import { axiosRequest } from '../main';
export default {
  name: 'login',
  data() {
    return{
      username: "",
      password: ""
    }
  },
  methods:{
    handleSubmit(){
      this.$store.dispatch('loginFromForm', {
        username: this.username,
        password: this.password
      }).then(({data})=>{
        let token = data.access_token
        axiosRequest.defaults.headers.Authorization = `Bearer ${token}`
        localStorage.setItem("token", token)
        this.$router.push('admin')
      })
    }
  }
}
</script>
