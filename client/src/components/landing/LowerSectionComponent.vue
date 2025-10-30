<template>
    <div>
      <div class="main-div">
        <div class="lower-image">
          <div class="text-div">
            <h5><router-link class="text" to="/data">The Data</router-link></h5>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
</script>

<style scoped>
.main-div {
  margin-bottom: 50px;
}

.lower-image {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background: url("../../assets/images/black_and_white_image.jpg") center/contain no-repeat;
  height: 1000px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
  background-color: #000; /* optional: fill empty space with a color */
}

.text-div {
  background-color: rgba(0, 0, 0, 0.7);
  padding: 5%;
  border-radius: 100%;
}

.text {
  color: white;
  font-size: 3em;
  text-transform: uppercase;
}


</style>