<template>
    <div>
      <div class="jumbotron jumbo-image">
        <div class="text-div-jumbotron">
          <h1 class="display-4 center">Everest Death Study</h1>
          <hr>
          <p class="lead center">A project to examine climbing deaths on Mt. Everest</p>
        </div>
      </div>
    </div>
</template>

<script>
</script>

<style scoped>
.text-div-jumbotron {
  background-color: rgba(0, 0, 0, 0.6);
  color: white;
  padding: 3%;
  border-radius: 12px;
  text-transform: uppercase;
}

.jumbo-image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: url("../../assets/images/everest.jpg") center/cover no-repeat;
  height: 800px;
}

</style>