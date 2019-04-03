<template>
  <div>
    <h2>Questions <span @click="handleClick">+</span></h2>
    <QuestionInfo v-for="question in questions" :key="question.id" :question="question"/>
        <div v-if="toggleForm" class="post-form">
            <button @click="handleClick" class="close-button">&times;</button>
            <h2>Add New Question</h2>
            <form @submit.prevent="handleSubmit">
                <input v-model="body" placeholder="question">
                <input type="submit"/>
            </form>
        </div>
    </div>
</template>

<script>
import { axiosRequest } from "../main"

import QuestionInfo from "../components/QuestionInfo"
export default {
  components: {
      QuestionInfo
  },
  data(){
    return {
        questions: [],
        body: "",
        toggleForm: false
    }
  },
  methods: {
    handleClick(){
          this.toggleForm = !this.toggleForm
    },
    handleSubmit(){
        axiosRequest.post('/question',{
            body: this.body
        })
        .then(({data})=>{
            this.questions.push(data)
            this.toggleForm = !this.toggleForm
        })
      }
  },
  mounted(){
    axiosRequest.get('/question')
      .then(({data})=>{ this.questions = data.objects})
  }
}
</script>