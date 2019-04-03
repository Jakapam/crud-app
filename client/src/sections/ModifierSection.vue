<template>
  <div>
    <h3>Modifiers  <span @click="handleClick">+</span></h3>
    <div :key="modifiers.length">
      <span v-for="modifier in modifiers" :key="modifier.id">
        <ModifierInfo :modifier="modifier"/>
        <button @click="handleDelete" :value="modifier.id">Delete Me</button>
      </span>
    </div>      
      <div v-if="toggleForm" class="post-form">
          <button @click="handleClick" class="close-button">&times;</button>
          <h2>Add New Modifier for Question:</h2>
          <h3>{{ question.body}}</h3>
          <form @submit.prevent="handleSubmit">
              <select v-model="token_id">
                <option v-for="token in tokens" :key="token.id" :value="token.id">{{token.name}}</option>
              </select>
              Yes:
              <input v-model="yesValue" type="number">
              No:
              <input v-model="noValue" type="number">
              <input type="submit"/>
          </form>
      </div>
  </div>
</template>

<script>
import ModifierInfo from "../components/ModifierInfo"
import {axiosRequest} from "../main"
export default {
  components: {
      ModifierInfo
  },
  computed:{
    tokens(){
      return this.$store.state.tokens
    }
  },
  data(){
      return{
        toggleForm: false,
        token_id: null,
        yesValue: 0,
        noValue: 0
      }
  },
  methods: {
    handleClick(){
          this.toggleForm = !this.toggleForm
    },
    handleDelete(e){
      axiosRequest.delete(`/modifier/${e.target.value}`).then(()=>{
        this.$store.dispatch('getManyResources',{resource:"question"})
      })
    },
    handleSubmit(){  
        axiosRequest.post('/modifier',{
            question_id: this.question.id,
            yes_modifier: this.yesValue,
            no_modifier: this.noValue,
            token_id: this.token_id
        })
        .then(({data})=>{
            this.modifiers.push(data)
            this.toggleForm = !this.toggleForm
        }).catch((err)=>{
          console.log(err)
        })
      }
  },
  props:{
        modifiers: Array,
        question: Object
    }
}
</script>