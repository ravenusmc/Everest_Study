<template>
  <div>
    <div ref="HeatMapCauseLocation"></div>
    <div id="popup">
      <div id="popupContent" class="popup-scroll"></div>
      <button @click="closePopup">Close</button>
    </div>
  </div>
</template>

<script>

export default {
  name: "CauseLocationHeatMap",
  computed: {
    ...mapGetters("datapage", [
      "heatMapCauseLocationData",
    ]),
  },
}

</script>