<template>
  <div id="app">
    <div class="main-project-div">
      <JumbotronComponent />
    </div>
    <!-- <img alt="Vue logo" src="./assets/logo.png"> -->

  </div>
</template>

<script>
import JumbotronComponent from './components/landing/JumbotronComponent.vue'

export default {
  name: 'App',
  components: {
    JumbotronComponent
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
