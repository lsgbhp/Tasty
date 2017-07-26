<template>
  <div id="app">
    <img id="avatar" src="./assets/avatar.jpg">
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'app'
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  margin: auto;
  max-width: 768px;
}
#avatar {
  width: 25%;
  max-width: 200px;
  border-radius: 50%;
  display: block;
  margin: 16px auto;
}
</style>
