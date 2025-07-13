<template>
    <div>
      <div ref="statesGraph"></div>
    </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "StatesGraph",
  computed: {
    ...mapGetters("datapage", [
      "deathsByStates",
    ]),
  },
  watch: {
    deathsByStates: {
      handler: "buildStateGraph",
      deep: true,
    },
  },
  mounted() {
    this.buildStateGraph();
  },  
  methods: {
    buildStateGraph() {

      // Clear previous SVG elements
      d3.select(this.$refs.statesGraph).select("svg").remove();
      
      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div
      let svg = d3
        .select(this.$refs.statesGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      // Add X axis
      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.deathsByStates.map((d) => d[0]))
        .padding(0.2);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Add Y axis
      let y = d3
        .scaleLinear()
        .domain([0, d3.max(this.deathsByStates, (d) => d[1])])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Create a tooltip div
      let tooltip = d3
        .select(this.$refs.statesGraph)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute");
    
        // Tooltip functions
      let showTooltip = function (event, d) {
        tooltip
          .style("opacity", 1)
          .html("Nationality: " + d[0] + "<br>Number of Deaths: " + d[1])
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 10 + "px");
      };

      let moveTooltip = function (event) {
        tooltip
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 10 + "px");
      };

      let hideTooltip = function () {
        tooltip.style("opacity", 0);
      };

      // Add bars
      let bars = svg
        .selectAll("rect")
        .data(this.deathsByStates);
      
      // Enter new bars
      bars
        .enter()
        .append("rect")
        .attr("x", (d) => x(d[0]))
        .attr("y", height) // Initial position at the bottom of the chart
        .attr("width", x.bandwidth())
        .attr("height", 0) // Initial height 0 (so it grows with the animation)
        .attr("fill", "#121212")
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip)
        .transition() // Apply transition for the animation
        .duration(1500)
        .attr("y", (d) => y(d[1])) // Final Y position
        .attr("height", (d) => height - y(d[1])); // Final height after transition
      
      // Add X axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10) // Adjusted y position to be within the SVG
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Nationality");
      
      // Add Y axis label
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Death Count");

      // Add title
      svg
        .append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10) // Adjusted y position to be within the SVG
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Deaths by Nation-State");
    }
  },

}

</script>
