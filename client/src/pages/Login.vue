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
export default {
  
  name: 'login',
  mounted(){
    
  },
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
      })
    }
  }
}
</script>
