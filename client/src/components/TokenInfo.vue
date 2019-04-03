<template>
  <div>
      <span style="font-weight:bold">{{token.name}}: </span>
      <span>{{token.value}}</span>
  </div>
</template>

<script>
export default {
  name: 'tokeninfo',
  props: {
    token: Object
  }
}
</script>