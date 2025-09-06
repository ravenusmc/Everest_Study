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
import * as d3 from "d3";
import { mapGetters, mapActions } from "vuex";

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
    ...mapActions("datapage", ["getDataForDrillDown"]),
    async handleBarClick(d) {

      //Prepare the payload
      const payload = { month: d[0]};
      
      // Await the response from the testMe action
      const response = await this.getDataForDrillDown(payload);
      console.log(response)

      //Function to create a table from JSON data
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
      content.innerHTML = `${'Month : ' + d[0]}<br>${createTableFromJson(response)}`;

      popup.style.display = "block";
      popup.style.top = `${event.clientY + 10}px`;
      popup.style.left = `${event.clientX + 10}px`;
    },
    buildDeathByMonthGraph() {
      // Clear previous SVG elements
      d3.select(this.$refs.DeathsByMonthGraph).select("svg").remove();

      // set the dimensions and margins of the graph
      let margin = { top: 50, right: 30, bottom: 50, left: 70 };
      let width = 460 - margin.left - margin.right;
      let height = 400 - margin.top - margin.bottom;

      // append the svg object to the div
      let svg = d3
        .select(this.$refs.DeathsByMonthGraph)
        .append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      // X axis (using scalePoint for even spacing of categories)
      let x = d3
        .scalePoint()
        .range([0, width])
        .domain(this.deathsByMonth.map((d) => d[0]))
        .padding(0.5);

      svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

      // Y axis
      let y = d3
        .scaleLinear()
        .domain([0, d3.max(this.deathsByMonth, (d) => d[1])])
        .range([height, 0]);

      svg.append("g").call(d3.axisLeft(y));

      // Tooltip
      let tooltip = d3
        .select(this.$refs.DeathsByMonthGraph)
        .append("div")
        .style("opacity", 0)
        .attr("class", "tooltip")
        .style("background-color", "white")
        .style("border", "solid")
        .style("border-width", "1px")
        .style("border-radius", "5px")
        .style("padding", "10px")
        .style("position", "absolute");

      let showTooltip = function (event, d) {
        tooltip
          .style("opacity", 1)
          .html("Month: " + d[0] + "<br>Deaths: " + d[1])
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

      // Create the line generator
      let line = d3.line()
        .x(d => x(d[0]))
        .y(d => y(d[1]))
        .curve(d3.curveMonotoneX); // Optional: makes the line smooth

      // Add the line path
      svg.append("path")
        .datum(this.deathsByMonth)
        .attr("fill", "none")
        .attr("stroke", "#121212")
        .attr("stroke-width", 2)
        .attr("d", line);

      // Add circles for each data point
      svg.selectAll("circle")
        .data(this.deathsByMonth)
        .enter()
        .append("circle")
        .attr("cx", d => x(d[0]))
        .attr("cy", d => y(d[1]))
        .attr("r", 4)
        .attr("fill", "#121212")
        .on("mouseover", showTooltip)
        .on("mousemove", moveTooltip)
        .on("mouseleave", hideTooltip)
        .on("click", async (event, d) => {
          await this.handleBarClick(d);
        });

      // X axis label
      svg.append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", height + margin.bottom - 10)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Month");

      // Y axis label
      svg.append("text")
        .attr("text-anchor", "middle")
        .attr("transform", "rotate(-90)")
        .attr("x", -height / 2)
        .attr("y", -margin.left + 20)
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .text("Death Count");

      // Title
      svg.append("text")
        .attr("text-anchor", "middle")
        .attr("x", width / 2)
        .attr("y", -margin.top / 2 + 10)
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("Deaths by Month (Graph 5)");
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