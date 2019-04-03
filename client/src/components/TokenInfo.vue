<template>
  <div>
      <span style="font-weight:bold">{{token.name}}: </span>
      <span>{{token.value}}</span>
  </div>
</template>

<script>
import {axiosRequest} from '../main'
export default {
  name: 'tokeninfo',
  props: {
    token: Object
  }
}
</script>