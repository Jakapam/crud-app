<template>
  <div>
      <h4>{{tokenName}}</h4>
      <span>Yes: {{modifier.yes_modifier}} </span>
      <span>No: {{modifier.no_modifier}} </span>
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