<template>
  <div class="states-graph-container">
    <div ref="statesGraph" class="graph"></div>

    <!-- Popup -->
    <div id="popup">
      <div id="popupContent" class="popup-scroll"></div>
      <button @click="closePopup">Close</button>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "StatesGraph",
  computed: {
    ...mapGetters("datapage", ["deathsByStates", "startDate"]),
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
    ...mapActions("datapage", ["getDataForDrillDown"]),

    async handleBarClick(d) {
      // Prepare payload
      const payload = { state: d[0] };
      const response = await this.getDataForDrillDown(payload);

      // Convert data to table
      function createTableFromJson(data) {
        let table =
          '<table border="1" cellpadding="4" cellspacing="0">' +
          '<tr><th>Name</th><th>Age</th><th>Year Missing</th>' +
          '<th>Expedition</th><th>Cause of Death</th><th>Location</th></tr>';

        data.forEach((row) => {
          const year = row.Date ? new Date(row.Date).getFullYear() : "Unknown";
          const age = row.Age !== null && row.Age !== undefined && row.Age !== "nan"
            ? row.Age
            : "Unknown";
          table += `<tr>
                      <td>${row.Name}</td>
                      <td>${age}</td>
                      <td>${year}</td>
                      <td>${row.Expedition}</td>
                      <td>${row.Cause_of_Death}</td>
                      <td>${row.Location}</td>
                    </tr>`;
        });

        table += "</table>";
        return table;
      }

      // Show popup centered
      const popup = document.getElementById("popup");
      const content = document.getElementById("popupContent");
      content.innerHTML = `Missing people from ${d[0]}<br>${createTableFromJson(response)}`;
      popup.style.display = "block"; // CSS handles centering
    },

    closePopup() {
      const popup = document.getElementById("popup");
      if (popup) popup.style.display = "none";
    },

    buildStateGraph() {
      // Clear old SVG
      d3.select(this.$refs.statesGraph).selectAll("*").remove();

      const margin = { top: 50, right: 30, bottom: 50, left: 70 };
      const width = 460 - margin.left - margin.right;
      const height = 400 - margin.top - margin.bottom;

      const svg = d3
        .select(this.$refs.statesGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", `translate(${margin.left},${margin.top})`);

      // X axis
      const x = d3.scaleBand()
        .range([0, width])
        .domain(this.deathsByStates.map(d => d[0]))
        .padding(0.2);
      svg.append("g")
        .attr("transform", `translate(0,${height})`)
        .call(d3.axisBottom(x));

      // Y axis
      const y = d3.scaleLinear()
        .domain([0, d3.max(this.deathsByStates, d => d[1])])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Tooltip div
      const tooltip = d3.select(this.$refs.statesGraph)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("position", "absolute")
        .style("background-color", "white")
        .style("border", "1px solid #ccc")
        .style("padding", "8px")
        .style("border-radius", "5px");

      const showTooltip = (event, d) => {
        tooltip
          .style("opacity", 1)
          .html(`State: ${d[0]}<br>Number of Deaths: ${d[1]}`)
          .style("left", event.pageX + 10 + "px")
          .style("top", event.pageY - 10 + "px");
      };
      const moveTooltip = (event) => {
        tooltip.style("left", event.pageX + 10 + "px").style("top", event.pageY - 10 + "px");
      };
      const hideTooltip = () => {
        tooltip.style("opacity", 0);
      };

      // Bars
      svg.selectAll("rect")
        .data(this.deathsByStates)
        .enter()
        .append("rect")
        .attr("x", d => x(d[0]))
        .attr("y", height)
        .attr("width", x.bandwidth())
        .attr("height", 0)
        .attr("fill", "#121212")
        .on("click", (event, d) => this.handleBarClick(d, event))
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip)
        .transition()
        .duration(1500)
        .attr("y", d => y(d[1]))
        .attr("height", d => height - y(d[1]));

      // Labels
      svg.append("text")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("State");

      svg.append("text")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Death Count");

      svg.append("text")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10)
        .attr("text-anchor", "middle")
        .attr("font-weight", "bold")
        .text("Deaths by State (Graph 1)");
    },
  },
};
</script>

<style>
div[ref="statesGraph"] {
  position: relative;
  z-index: 0;
}

#popup {
  z-index: 1000;
  display: none;
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: white;
  border: 1px solid #ccc;
  padding: 20px;
  max-width: 90vw;
  max-height: 80vh;
  overflow: hidden;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.popup-scroll {
  max-height: 60vh;
  overflow-y: auto;
  margin-bottom: 10px;
}

#popup table {
  border-collapse: collapse;
  width: 100%;
}

#popup th,
#popup td {
  padding: 8px;
  text-align: left;
}

th {
  border: 2px solid black;
}

tr {
  border: 2px solid black;
}

#popup th {
  background-color: #dfd3d3;
}

button {
  border: 2px solid black;
  padding: 8px;
  border-radius: 14px;
}

button:hover {
  background-color: rgb(14, 8, 8);
  color: white;
}
</style>
