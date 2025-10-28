<template>
  <div class="flex justify-center items-center p-6">
    <form
      class="bg-white shadow-lg rounded-2xl p-8 max-w-7xl w-full grid gap-6 md:grid-cols-3 lg:grid-cols-4"
      @submit.prevent="submitNumberStatesToServer"
    >
      <!-- Number of States -->
      <div>
        <label class="block text-gray-700 font-medium mb-2">
          Select Number of States to See: (Graph 1)
        </label>
        <select
          v-model="numberOfStates"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        >
          <option disabled value="">Please select one</option>
          <option v-for="state in numberOfStatesOptions" :key="state" :value="state">
            {{ state }}
          </option>
        </select>
      </div>

      <!-- Number of Bins -->
      <div>
        <label class="block text-gray-700 font-medium mb-2">
          Enter Number of bins for range of years: (Graph 2)
        </label>
        <select
          v-model="numberOfBins"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        >
          <option disabled value="">Please select one</option>
          <option v-for="bins in numberOfBinsOptions" :key="bins" :value="bins">
            {{ bins }}
          </option>
        </select>
      </div>

      <!-- Number of Expeditions -->
      <div>
        <label class="block text-gray-700 font-medium mb-2">
          Enter Number of Expeditions: (Graph 3)
        </label>
        <select
          v-model="numberOfExpeditions"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        >
          <option disabled value="">Please select one</option>
          <option v-for="bins in numberOfExpeditionsOptions" :key="bins" :value="bins">
            {{ bins }}
          </option>
        </select>
      </div>

      <!-- Causes of Death -->
      <div>
        <label class="block text-gray-700 font-medium mb-2">
          Enter Number to see more causes of death: (Graph 4)
        </label>
        <select
          v-model="numberOfCausesOfDeath"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        >
          <option disabled value="">Please select one</option>
          <option
            v-for="bins in numberOfCausesOfDeathOptions"
            :key="bins"
            :value="bins"
          >
            {{ bins }}
          </option>
        </select>
      </div>

      <!-- Start Date -->
      <div>
        <label for="startDate" class="block text-gray-700 font-medium mb-2">
          Start Date:
        </label>
        <input
          type="date"
          id="startDate"
          v-model="startDate"
          :min="minDate"
          :max="maxDate"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        />
      </div>

      <!-- End Date -->
      <div>
        <label for="endDate" class="block text-gray-700 font-medium mb-2">
          End Date:
        </label>
        <input
          type="date"
          id="endDate"
          v-model="endDate"
          :min="minDate"
          :max="maxDate"
          class="w-full rounded-xl border border-gray-300 px-4 py-2 text-gray-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 transition"
        />
      </div>

      <!-- Submit button -->
      <div class="md:col-span-3 lg:col-span-4 pt-4">
        <button
          class="w-full bg-indigo-600 text-white font-semibold py-3 rounded-xl shadow-md hover:bg-indigo-700 transition"
          type="submit">
          Submit
        </button>
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
      numberOfCausesOfDeath: 3,
      numberOfCausesOfDeathOptions: [1,2,3,4,5,6,7,8,9,10],
      numberOfExpeditions: 3, 
      numberOfExpeditionsOptions:[1,2,3,4,5,6,7,8,9,10],
      startDate: "",
      endDate: "",
      minDate: "1921-06-05",
      maxDate: "2025-05-15",
    };
  },
  methods: {
    ...mapActions("datapage", ["getDataBasedOnFilters"]),
    submitNumberStatesToServer(event) {
      event.preventDefault();
      if (this.numberOfStates <= 0) {
        alert("Please Select a year greater than 0");
      } else if (this.numberOfStates > 10) {
        alert("Please Select a Year Less than or equal to 10");
      } else if (this.numberOfBins <= 0) {
        alert("Please enter a number greater than 0");
      } else if (!this.startDate || !this.endDate) {
        alert("Please select both start and end dates.");
      } else if (this.startDate > this.endDate) {
        alert("Start date cannot be after end date.");
      } else {
        const payload = {
          numberOfStates: this.numberOfStates,
          numberOfBins: this.numberOfBins,
          numberOfExpeditions: this.numberOfExpeditions,
          numberOfCausesOfDeath: this.numberOfCausesOfDeath,
          firstDate: this.startDate,
          lastDate: this.endDate,
        };
        this.getDataBasedOnFilters({ payload });
      }
    },
  },
};
</script>

<style scoped>
form {
  /* Overriding Tailwind’s vertical spacing */
  display: grid;
}
</style>
