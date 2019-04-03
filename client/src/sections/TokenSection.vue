<template>
  <div>
    <h2>Tokens  <span @click="handleClick">+</span></h2>
    <TokenInfo v-for="token in tokens" :key="token.id" :token="token"/>
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
