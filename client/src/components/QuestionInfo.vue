<template>
  <div>
    <h2 style="font-weight:bold">{{question.body}}</h2>
    <ModifierSection :question="question" :modifiers="question.modifiers"/>
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