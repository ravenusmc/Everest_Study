<template>
    <div>
        <div class="filter-div">
            <StateFilter />
        </div>
        <div class="graphs-div">
            <StatesGraph />
            <DeathsGraph />
            <ExpeditionsGraph />
        </div>
    </div>
</template>

<script>
import StateFilter from '@/components/filters/StateFilter.vue'
import StatesGraph from '@/components/graphs/StatesGraph.vue'
import DeathsGraph from '@/components/graphs/DeathsGraph.vue'
import ExpeditionsGraph from '@/components/graphs/ExpeditionsGraph.vue'

export default {
	name: "DataView",
	components: {
    StatesGraph,
    StateFilter,
    DeathsGraph,
    ExpeditionsGraph
  },
};

</script>

<style scoped>

.filter-div {
    border: 2px solid red;
}

</style>

