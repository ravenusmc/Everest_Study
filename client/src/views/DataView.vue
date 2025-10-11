<template>
    <div>
        <div>
            <OverView />
        </div>
        <div class="filter-div">
            <MainFilter />
        </div>
          <div class="first-row">
            <StatesGraph />
            <DeathsGraph />
            <ExpeditionsGraph />
          </div>
          <div class="second-row">
            <CauseOfDeathGraph />
            <DeathsByMonthGraph />
          </div>
        <!-- May use this at a future date -->
        <!-- <div class="heat-map-graphs">
            <HeatMapCauseLocation />
        </div> -->
    </div>
</template>

<script>
import OverView from '@/components/data/OverView.vue'
import MainFilter from '@/components/filters/MainFilter.vue'
import StatesGraph from '@/components/graphs/StatesGraph.vue'
import DeathsGraph from '@/components/graphs/DeathsGraph.vue'
import ExpeditionsGraph from '@/components/graphs/ExpeditionsGraph.vue'
import CauseOfDeathGraph from '@/components/graphs/CauseOfDeathGraph.vue'
import DeathsByMonthGraph from '@/components/graphs/DeathsByMonth.vue'
// May use this at a future date
// import HeatMapCauseLocation from '@/components/graphs/HeatMapCauseLocation.vue'

export default {
	name: "DataView",
	components: {
    StatesGraph,
    MainFilter,
    DeathsGraph,
    ExpeditionsGraph,
    CauseOfDeathGraph,
    DeathsByMonthGraph,
    OverView,
    // May use this at a future date
    // HeatMapCauseLocation,
  },
};

</script>

<style scoped>

.first-row {
  display: grid; 
  grid-template-columns: 1fr 1fr 1fr;
}

.second-row {
  display: grid;
  grid-template-columns: auto auto; /* make them only as wide as their content */
  justify-content: center; /* center horizontally */
  align-items: center; /* center vertically (if row taller) */
  gap: 15rem; /* optional space between graphs */
}


</style>

