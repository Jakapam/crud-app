<template>
  <div v-if="tokenName">
      <span style="font-weight:bold">{{token.name}}: </span>
      <span>{{token.value}}</span>
      <span><button @click="handleClick">Delete Me</button></span>
  </div>
</template>

<script>
import {axiosRequest} from '../main'
export default {
  name: 'tokeninfo',
  computed:{
    tokenName(){
      return this.token.name
    } 
  },
  methods:{
    handleClick(){
      axiosRequest.delete(`/token/${this.token.id}`).then(()=>{
        this.token = null
      })
    }
  },
  props: {
    token: Object
  }
}
</script>