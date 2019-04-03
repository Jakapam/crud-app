<template>
  <div>
    <div>{{resourceData}}</div>
  </div>
</template>

<script>
import { axiosRequest } from "../main"

export default {
  name: 'resource',
  data(){
    return{
      resourceData: []
    }
  },
  mounted(){
    axiosRequest.get(`${this.resourceName}`)
      .then(({data})=>{ this.resourceData = data.objects})
  },
  props: {
    resourceName: String
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
