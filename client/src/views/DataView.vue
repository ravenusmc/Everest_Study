<template>
    <div>
        <div>
            <OverView />
        </div>
        <div class="filter-div">
            <MainFilter />
        </div>
        <div class="graphs-div">
            <StatesGraph />
            <DeathsGraph />
            <ExpeditionsGraph />
            <CauseOfDeathGraph />
            <DeathsByMonthGraph />
        </div>
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
  },
};

</script>

<style scoped>

.filter-div {
    border: 2px solid red;
}

.graphs-div {
  display: grid; 
  grid-template-columns: 1fr 1fr 1fr;
}

</style>

