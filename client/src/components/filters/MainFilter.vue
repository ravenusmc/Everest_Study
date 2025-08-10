<template>
    <div>
      <form>
        <div>
          <label for="ammo">Select Number of States to See:</label>
          <select v-model="numberOfStates">
            <option disabled value="">Please select one</option>
            <option v-for="state in numberOfStatesOptions" :key="state" :value="state">
              {{ state }}
            </option>
          </select>
        </div>
        <div>
          <label>Enter Number of bins for range of years:</label>
          <select v-model="numberOfBins">
            <option disabled value="">Please select one</option>
            <option v-for="bins in numberOfBinsOptions" :key="bins" :value="bins">
              {{ bins }}
            </option>
          </select>
        </div>
        <div>
          <label for="startDate">Start Date:</label>
            <input
              type="date"
              id="startDate"
              v-model="startDate"
              :min="minDate"
              :max="maxDate"
            /><br><br>

            <label for="endDate">End Date:</label>
            <input
              type="date"
              id="endDate"
              v-model="endDate"
              :min="minDate"
              :max="maxDate"
            /><br><br>
        </div>
        <div class="form-group">
          <button class='styled-button' type="button" @click="submitNumberStatesToServer">Submit</button>
        </div>
      </form>
    </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "MainFilter",
  data() {
    return {
      numberOfStatesOptions: [1,2,3,4,5,6,7,8,9,10],
      numberOfStates: 3, 
      numberOfBinsOptions: [5,10,12,15,18,21],
      numberOfBins: 10,
      startDate: "",
      endDate: "",
      minDate: "1921-06-05",
      maxDate: "2025-05-15",
    };
  },
  methods: {
    ...mapActions("datapage", ["getDataBasedOnFilters"]),
    submitNumberStatesToServer() {
      event.preventDefault();
      console.log(this.startDate)
      if (this.numberOfStates <= 0) {
        alert("Please Select a year greater than 0");
      } 
      else if (this.numberOfStates > 10) {
        alert("Please Select a Year Less than or equal to 10");
      } 
      else if (this.numberOfBins <= 0) {
        alert("Please enter a number greater than 0")
      }
      else if (!this.startDate || !this.endDate) {
        alert("Please select both start and end dates.");
      }else if (this.startDate > this.endDate) {
        alert("Start date cannot be after end date.");
      }
      else {
        const payload = {
          numberOfStates: this.numberOfStates,
          numberOfBins: this.numberOfBins,
          firstDate: this.startDate, 
          lastDate: this.endDate,
        };
        this.getDataBasedOnFilters({ payload });
      }
    },
  },
};
</script>

<style></style>