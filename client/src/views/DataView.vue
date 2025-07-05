<template>
    <div>
        <div class="filter-div">
            <StateFilter />
        </div>
        <div class="graphs-div">
            <StatesGraph />
        </div>
    </div>
</template>

<script>
import StateFilter from '@/components/filters/StateFilter.vue'
import StatesGraph from '@/components/graphs/StatesGraph.vue'

export default {
	name: "DataView",
	components: {
    StatesGraph,
    StateFilter,
  },
};

</script>

<style scoped>

.filter-div {
    border: 2px solid red;
}

</style>

