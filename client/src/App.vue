<template>
  <div ref="app" id="app">
    <router-view/>
  </div>
</template>

<script>
import { axiosRequest } from "./main"

export default {
  name: 'app',
  data() {
    return{}
  }
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: left;
    color: #2c3e50;
    margin-top: 60px;
  }

  .post-form {
      z-index: 1000;
      background-color: #eeeeee;
      width: 40vw;
      height: 40vh;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      display: flex;
      flex-flow: column nowrap;
      justify-content: center;
      align-items: center;
      overflow: hidden;
      box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.2);
  }

  .close-button {
      cursor: pointer;
      position: absolute;
      top: 10px;
      right: 10px;
      background: none;
      border: none;
      outline: none;
      font-size: 2em;
  }
</style>
