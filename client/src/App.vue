<template>
  <div class="page-wrapper">
    <NavBar />
    <router-view /> <!-- or your page content -->
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
}

.page-wrapper {
  min-height: 100vh; /* fill entire viewport */
  display: flex;
  flex-direction: column;
}

router-view, main {
  flex: 1; /* pushes footer down */
}
</style>
