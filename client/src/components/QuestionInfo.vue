<template>
  <div>
    <span style="font-weight:bold">{{question.body}}</span>
    <h3>Modifications</h3>
    <ModifierSection :modifiers="question.modifiers"/>
  </div>
</template>

<script>
import ModifierSection from '../sections/ModifierSection'
export default {
  name: 'questioninfo',
  components: {
      ModifierSection
    },
  props: {
    question: Object
  }
}
</script>