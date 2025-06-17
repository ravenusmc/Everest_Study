<template>
  <div>
    <div class="main-project-div">
      <JumbotronComponent />
      <MidSectionComponent />
    </div>
  </div>
</template>

<script>
import JumbotronComponent from '../components/landing/JumbotronComponent.vue'
import MidSectionComponent from '../components/landing/MidSectionComponent.vue'

export default {
  name: "HomeView",
  components: {
    JumbotronComponent,
    MidSectionComponent,
  }
};
</script>

<style>

.main-project-div {
  margin: 0 5%;
}

</style>