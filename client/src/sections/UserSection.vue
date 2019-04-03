<template>
  <div>
    <UserInfo v-for="user in users" :key="user.id" :user="user"/>
  </div>
</template>

<script>
import { axiosRequest } from "../main"

import UserInfo from "../components/UserInfo"
export default {
  components: {
      UserInfo
  },
  data(){
    return {
        users: []
    }
  },
  mounted(){
    axiosRequest.get('/user')
      .then(({data})=>{ this.users = data.objects})
  }
}
</script>