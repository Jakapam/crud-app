<template>
  <div>
    <UserSection/>
    <TokenSection/>
    <QuestionSection/>
  </div>
</template>

<script>
import Resource from "../components/Resource"
import UserSection from "../sections/UserSection"
import TokenSection from "../sections/TokenSection"
import QuestionSection from "../sections/QuestionSection"

export default {
  name: 'admin',
  mounted(){
    this.$store.dispatch('getManyResources',{resource:"token"})
    this.$store.dispatch('getManyResources',{resource:"question"})
  },
  components: {
    Resource,
    UserSection,
    TokenSection,
    QuestionSection
  },
  props: {
    msg: String
  }
}
</script>

