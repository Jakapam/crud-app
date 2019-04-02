<template>
  <div>
    <div v-for="resource in resources" :key="resource">
        <Resource :resourceName="resource"/>
    </div> 
  </div>
</template>

<script>
import { axiosRequest } from "../main"
import Resource from "./Resource"

export default {
  name: 'admin',
  components: {
    Resource
  },
  data(){
    return {
       resources: ["user","question","token"]
    }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
