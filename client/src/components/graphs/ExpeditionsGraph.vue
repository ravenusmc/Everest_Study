<template>
    <div>
        <div ref="expeditionsGraph"></div>
        lki
    </div>
</template>

<script>
// import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "ExpeditionsGraph",
  computed: {
    ...mapGetters("datapage", [
      "deathsByExpedition",
    ]),
  },
  watch: {
    deathsByExpedition: {
      handler: "buildExpeditionGraph",
      deep: true,
    },
  },
  mounted() {
    this.buildExpeditionGraph();
  },  
  methods: {
    buildExpeditionGraph() {
    }
  }
}

</script>