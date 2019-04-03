<template>
  <div>
    <h2>Users</h2>
    <UserSection/>
    <h2>Tokens</h2>
    <TokenSection/>
    <h2>Questions</h2>
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
  components: {
    Resource,
    UserSection,
    TokenSection,
    QuestionSection
  },
  data(){
    return {
       resources: ["question"]
    }
  },
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
