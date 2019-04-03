<template>
  <div :key="tokenName" v-if="tokenName">
      <h4>{{tokenName}}</h4>
      <span>Yes: {{modifier.yes_modifier}} </span>
      <span>No: {{modifier.no_modifier}} </span>
      <span><button @click="handleClick">Delete Me</button></span>
  </div>
</template>

<script>
import { axiosRequest } from "../main"
export default {
  name: 'modifierinfo',
  mounted(){
      axiosRequest.get(`token/${this.modifier.token_id}`)
        .then(({data})=>{
            this.tokenName = data.name
        })
  },
  methods:{
    handleClick(){
      axiosRequest.delete(`/modifier/${this.modifier.id}`).then(()=>{
        this.tokenName = null
      })
    }
  },
  data(){
      return{
          tokenName: ""
      }
  },
  props: {
    modifier: Object
  }
}
</script>