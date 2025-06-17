<template>
  <div id="app">
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
    <NavBar />
    <router-view></router-view>
  </div>
</template>

<script>
import NavBar from "./components/common/NavBar.vue";

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>

.center {
  text-align: center;
}

.main-project-div {
  margin: 0 5%;
}

</style>
