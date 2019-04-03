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
