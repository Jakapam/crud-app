<template>
  <div>
    <h2>Tokens  <span @click="handleClick">+</span></h2>
    <span v-for="token in tokens" :key="token.name">
      <TokenInfo :key="token.id" :token="token"/>
      <button @click="handleDelete" :value="token.id">Delete Me</button>
    </span>
    <div v-if="toggleForm" class="post-form">
        <button @click="handleClick" class="close-button">&times;</button>
        <h2>Add New Token </h2>
        <form @submit.prevent="handleSubmit">
            <input v-model="name" placeholder="name">
        <input type="submit"/>
      </form>
    </div>
  </div>
</template>

<script>
import { axiosRequest } from "../main"

import TokenInfo from "../components/TokenInfo"
export default {
  components: {
      TokenInfo
  },
  computed:{
    tokens(){
      return this.$store.state.tokens
    }
  },
  data(){
    return {
        name: "",
        toggleForm: false
    }
  },
  methods: {
    handleClick(){
      this.toggleForm = !this.toggleForm
    },
    handleDelete(e){
      axiosRequest.delete(`/token/${e.target.value}`).then(()=>{
        this.$store.dispatch('getManyResources',{resource:"token"})
        this.$store.dispatch('getManyResources',{resource:"question"})
      })
    },
    handleSubmit(){
        axiosRequest.post('/token',{
            name: this.name
        })
        .then(({data})=>{
            this.tokens.push(data)
            this.toggleForm = !this.toggleForm
        })
      }
  }
}
</script>
