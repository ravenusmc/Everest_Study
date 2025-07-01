<template>
    <div>
        <div class="filter-div">

        </div>
        <div class="graphs-div">
            <StatesGraph />
        </div>
    </div>
</template>

<script>
import StatesGraph from '@/components/graphs/StatesGraph.vue'

export default {
	name: "DataView",
	components: {
    StatesGraph,
  },
};

</script>

<style scoped>

</style>

