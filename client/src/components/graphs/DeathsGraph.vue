<template>
    <div>
        <div ref="deathsGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "DeathsGraph",
  computed: {
    ...mapGetters("datapage", [
      "deathsByAge",
    ]),
  },
  mounted() {
    this.buildDeathGraph();
  }, 
  methods: {
    buildDeathGraph() {
      
      // Clear previous SVG elements
      d3.select(this.$refs.deathsGraph).select("svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div
      let svg = d3
        .select(this.$refs.deathsGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      // Add X axis
      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.deathsByAge.map((d) => d[0]))
        .padding(0.2);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));


    }
  } 
}

</script>