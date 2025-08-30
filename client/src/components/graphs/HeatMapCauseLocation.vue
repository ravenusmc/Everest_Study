<template>
  <div style="overflow:auto; max-height:800px;">
    <div ref="HeatMapCauseLocation"></div>
    <div id="popup">
      <div id="popupContent" class="popup-scroll"></div>
      <button @click="closePopup">Close</button>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters } from "vuex";

export default {
  name: "CauseLocationHeatMap",
  computed: {
    ...mapGetters("datapage", [
      "heatMapCauseLocationData",
    ]),
  },
  watch: {
    heatMapCauseLocationData: {
      handler: "buildCauseLocationHeatGraph",
      deep: true,
    },
  },
  mounted() {
    this.buildCauseLocationHeatGraph();
  },
  methods: {
    buildCauseLocationHeatGraph() {
      // Clear previous SVG
      d3.select(this.$refs.HeatMapCauseLocation).select("svg").remove();

      const data = this.heatMapCauseLocationData;
      if (!data || data.length === 0) return;

      const Locations = [...new Set(data.map(d => d.Location))];
      const Causes = [...new Set(data.map(d => d.Cause))];

      const margin = { top: 150, right: 30, bottom: 150, left: 200 };
      const width = Math.max(Causes.length * 50, 1000) - margin.left - margin.right;
      const height = Math.max(Locations.length * 25, 700) - margin.top - margin.bottom;

      const svg = d3.select(this.$refs.HeatMapCauseLocation)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // Scales
      const x = d3.scaleBand()
        .range([0, width])
        .domain(Causes)
        .padding(0.05);

      const y = d3.scaleBand()
        .range([height, 0])
        .domain(Locations)
        .padding(0.05);

      const color = d3.scaleSequential()
        .interpolator(d3.interpolateBlues)
        .domain([0, d3.max(data, d => d.Count)]);

      // Axes
      svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x))
        .selectAll("text")
        .attr("transform", "rotate(-60)")
        .style("text-anchor", "end")
        .style("font-size", "10px")
        .call(this.wrapText, x.bandwidth());

      svg.append("g")
        .call(d3.axisLeft(y))
        .selectAll("text")
        .style("font-size", "10px");

      // Tooltip
      const tooltip = d3.select("body")
        .append("div")
        .attr("class", "tooltip")
        .style("opacity", 0)
        .style("position", "absolute")
        .style("background", "#fff")
        .style("padding", "5px")
        .style("border", "1px solid #ccc")
        .style("border-radius", "4px");

      // Draw heatmap rectangles
      svg.selectAll()
        .data(data)
        .enter()
        .append("rect")
        .attr("x", d => x(d.Cause))
        .attr("y", d => y(d.Location))
        .attr("width", x.bandwidth())
        .attr("height", y.bandwidth())
        .style("fill", d => color(d.Count))
        .style("stroke", "#fff")
        .on("mouseover", function(event, d) {
          tooltip.transition().duration(200).style("opacity", 1);
          tooltip.html(`<strong>${d.Location}</strong><br>${d.Cause}: ${d.Count}`)
            .style("left", (event.pageX + 5) + "px")
            .style("top", (event.pageY - 28) + "px");
        })
        .on("mouseout", function() {
          tooltip.transition().duration(500).style("opacity", 0);
        });
    },

    wrapText(text, width) {
      text.each(function() {
        const textEl = d3.select(this),
              words = textEl.text().split(/\s+/).reverse(),
              lineHeight = 1.1; // ems
        let word, line = [], lineNumber = 0, y = textEl.attr("y"), dy = 0;
        let tspan = textEl.text(null).append("tspan").attr("x", 0).attr("y", y).attr("dy", dy + "em");

        while ((word = words.pop())){
          line.push(word);
          tspan.text(line.join(" "));
          if (tspan.node().getComputedTextLength() > width) {
            line.pop();
            tspan.text(line.join(" "));
            line = [word];
            tspan = textEl.append("tspan").attr("x", 0).attr("y", y).attr("dy", ++lineNumber * lineHeight + dy + "em").text(word);
          }
        }
      });
    },

    closePopup() {
      d3.select("#popup").style("display", "none");
    }
  }
}
</script>

<style scoped>
.tooltip {
  pointer-events: none;
}
</style>
