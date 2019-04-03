<template>
  <div>
    <ResponseInfo v-for="response in responses" :key="response.id" :response="response"/>
  </div>
</template>

<script>
import ResponseInfo from "../components/ResponseInfo"
export default {
  components: {
      ResponseInfo
  },
  props:{
        responses: Array
    }
}
</script>