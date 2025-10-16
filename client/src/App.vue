<template>
  <div id="app">
    <NavBar />
    <router-view :key="$route.fullPath"></router-view>
    <FootComponent />
  </div>
</template>


<script>
import NavBar from "./components/common/NavBar.vue";
import FootComponent from "@/components/common/FootComponent.vue";

export default {
  name: 'App',
  components: {
    NavBar,
    FootComponent,
  }
}
</script>

<style>

html, body {
  height: 100%;
  margin: 0;
  padding: 0;
}

.center {
  text-align: center;
}

/* .main-project-div {
  margin: 0 5%;
} */

</style>
