<template>
  <div>
    <TokenInfo v-for="token in tokens" :key="token.id" :token="token"/>
  </div>
</template>

<script>
import { axiosRequest } from "../main"

import TokenInfo from "../components/TokenInfo"
export default {
  components: {
      TokenInfo
  },
  data(){
    return {
        tokens: []
    }
  },
  mounted(){
    axiosRequest.get('/token')
      .then(({data})=>{ this.tokens = data.objects})
  }
}
</script>