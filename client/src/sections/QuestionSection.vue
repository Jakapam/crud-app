<template>
  <div>
    <QuestionInfo v-for="question in questions" :key="question.id" :question="question"/>
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
        questions: []
    }
  },
  mounted(){
    axiosRequest.get('/question')
      .then(({data})=>{ this.questions = data.objects})
  }
}
</script>