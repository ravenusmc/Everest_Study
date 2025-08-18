<template>
  <div>
    <div ref="CauseOfDeathGraph"></div>
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
  name: "CauseOfDeathGraph",
  computed: {
    ...mapGetters("datapage", [
      "causeOfDeath",
    ]),
  },
  watch: {
    causeOfDeath: {
      handler: "buildCauseOfDeathGraph",
      deep: true,
    },
  },
  mounted() {
    this.buildCauseOfDeathGraph();
  },  
  methods: {
    ...mapActions("datapage", ["getDataForDrillDown"]),
     async handleBarClick(d) {

      //Prepare the payload
      const payload = { cause_of_death: d[0]};

      // Await the response from the testMe action
      const response = await this.getDataForDrillDown(payload);
      
      // //Function to create a table from JSON data
      function createTableFromJson(data) {
        let table =
          '<table border="1" cellpadding="4" cellspacing="0">' +
          '<tr><th>Name</th><th>Age</th><th>Year Missing</th>' +
          '<th>Expedition</th><th>Cause of Death</th><th>Location</th>'+ 
          '</tr>';

        data.forEach((row) => {

          // Extract year from date
          let year = row.Date ? new Date(row.Date).getFullYear() : 'Unknown';

          // Handle missing fields
          let age = row.Age !== null && row.Age !== undefined && row.Age !== 'nan' ? row.Age : 'Unknown';

          // Add row to table
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

      // Display the popup with the count and response
      const popup = document.getElementById("popup");
      const content = document.getElementById("popupContent");
      content.innerHTML = `${'Cause of death: ' + d[0]}<br>${createTableFromJson(response)}`;

      popup.style.display = "block";
      popup.style.top = `${event.clientY + 10}px`;
      popup.style.left = `${event.clientX + 10}px`;
    },
    buildCauseOfDeathGraph() {

      // Clear previous SVG elements
      d3.select(this.$refs.CauseOfDeathGraph).select("svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div
      let svg = d3
        .select(this.$refs.CauseOfDeathGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      // Add X axis
      let x = d3
        .scaleBand()
        .range([0, width])
        .domain(this.causeOfDeath.map((d) => d[0]))
        .padding(0.2);
      svg
        .append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));
      
      // Add Y axis
      let y = d3
        .scaleLinear()
        .domain([0, d3.max(this.causeOfDeath, (d) => d[1])])
        .range([height, 0]);
      svg.append("g").call(d3.axisLeft(y));

      // Create a tooltip div
      let tooltip = d3
        .select(this.$refs.CauseOfDeathGraph)
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
          .html("Cause of Death: " + d[0] + "<br>Number of Deaths: " + d[1])
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
        .data(this.causeOfDeath);
      
      // Enter new bars
      bars
        .enter()
        .append("rect")
        .attr("x", (d) => x(d[0]))
        .attr("y", height) // Initial position at the bottom of the chart
        .attr("width", x.bandwidth())
        .attr("height", 0) // Initial height 0 (so it grows with the animation)
        .attr("fill", "#121212")
        .on("click", async (event, d) => {
          await this.handleBarClick(d);
        })
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
        .text("Cause of Death");
      
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
        .text("Causes of Death");
    },
  },
}
</script>

<style scoped>
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

#popup th, #popup td {
  padding: 8px;
  text-align: left;
}

#popup th {
  background-color: #f2f2f2;
}
</style>