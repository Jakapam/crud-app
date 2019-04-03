<template>
  <div>
    <ModifierInfo v-for="modifier in modifiers" :key="modifier.id" :modifier="modifier"/>
  </div>
</template>

<script>
import ModifierInfo from "../components/ModifierInfo"
export default {
  components: {
      ModifierInfo
  },
  props:{
        modifiers: Array
    }
}
</script>