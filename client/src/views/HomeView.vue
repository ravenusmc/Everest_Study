<template>
  <div>
    <div class="main-project-div">
      <JumbotronComponent />
      <MidSectionComponent />
      <LowerSectionComponent />
    </div>
  </div>
</template>

<script>
import JumbotronComponent from '../components/landing/JumbotronComponent.vue'
import MidSectionComponent from '../components/landing/MidSectionComponent.vue'
import LowerSectionComponent from '../components/landing/LowerSectionComponent.vue'

export default {
  name: "HomeView",
  components: {
    JumbotronComponent,
    MidSectionComponent,
    LowerSectionComponent,
  }
};
</script>

<style>

.main-project-div {
  margin: 0 5%;
}

</style>