<template>
  <div :key="tokenName" v-if="tokenName">
      <h4>{{tokenName}}</h4>
      <span>Yes: {{modifier.yes_modifier}} </span>
      <button @click="handleAdd" value="yes_modifier">+</button><button @click="handleSub" value="yes_modifier">-</button>
      <span>No: {{modifier.no_modifier}} </span>
      <button @click="handleAdd" value="no_modifier">+</button><button @click="handleSub" value="no_modifier">-</button>
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
    handleAdd(e){
      let newVals = {}
      newVals[e.target.value] = this.modifier[e.target.value] + 1
      axiosRequest.patch(`/modifier/${this.modifier.id}`, newVals)
        .then(()=>{
          this.$store.dispatch('getManyResources',{resource: "question"})
          this.$store.dispatch('getManyResources',{resource: "token"})
        })
    },
    handleSub(e){
      let newVals = {}
      newVals[e.target.value] = this.modifier[e.target.value] - 1
      axiosRequest.patch(`/modifier/${this.modifier.id}`, newVals)
        .then(()=>{
          this.$store.dispatch('getManyResources',{resource: "question"})
          this.$store.dispatch('getManyResources',{resource: "token"})
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