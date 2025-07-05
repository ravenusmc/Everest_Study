<template>
    <div>
      <form>
        <div>
          <label for="state">Enter Number of States to see:</label>
          <input v-model="numberOfStates" />
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
  name: "StateFilter",
  data() {
    return {
      numberOfStates: 3,
    };
  },
  methods: {
    ...mapActions("datapage", ["getDataBasedOnFilters"]),
    submitNumberStatesToServer() {
      event.preventDefault();
      if (this.numberOfStates <= 0) {
        alert("Please Select a year greater than 0");
      } else if (this.numberOfStates > 10) {
        alert("Please Select a Year Less than or equal to 10");
      } else {
        const payload = {
          numberOfStates: this.numberOfStates,
        };
        this.getDataBasedOnFilters({ payload });
      }
    },
  },
};
</script>

<style></style>