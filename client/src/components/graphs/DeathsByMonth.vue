<template>
    <div>
    <div ref="DeathsByMonthGraph"></div>
    <div id="popup">
      <div id="popupContent" class="popup-scroll"></div>
      <button @click="closePopup">Close</button>
    </div>
    </div>
</template>

<script>
// import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "DeathsByMonthGraph",
  computed: {
    ...mapGetters("datapage", [
      "deathsByMonth",
    ]),
  },
  watch: {
    deathsByMonth: {
      handler: "buildDeathByMonthGraph",
      deep: true,
    },
  },
   mounted() {
    this.buildDeathByMonthGraph();
  },  
  methods: {
  },
}

</script>

<style scoped>
</style>