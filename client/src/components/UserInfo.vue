<template>
  <div>
      <span style="font-weight:bold">{{user.username}} </span>
      <span>| Email: {{user.username}} | Admin: {{user.is_admin ? "Yes":"No"}}</span>
  </div>
</template>

<script>
export default {
  name: 'userinfo',
  props: {
    user: Object
  }
}
</script>