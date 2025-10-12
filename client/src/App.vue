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

.center {
  text-align: center;
}

.main-project-div {
  margin: 0 5%;
}

</style>
