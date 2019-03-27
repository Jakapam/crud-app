<template>
  <div id="app">
    <HelloWorld :msg="msg"/>
  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import { axiosRequest } from "./main"

export default {
  name: 'app',
  mounted(){
    axiosRequest()
      .then(({data})=>{
        this.msg = data.msg
      })
  },
  components: {
    HelloWorld
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
