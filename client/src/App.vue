<template>
  <div id="app">
    <Admin/>
  </div>
</template>

<script>
import Admin from './components/Admin.vue'
import { axiosRequest } from "./main"

export default {
  name: 'app',
  mounted(){
    axiosRequest("/user")
      .then(({data})=>{
        console.log(data)
      })
      .catch((e)=>{
        console.log(e)
      })
  },
  components: {
    Admin
  },
  data() {
    return{
      msg: "Loading"
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
