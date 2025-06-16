<template>
    <div>
      <div class="main-div">
        <div class="pic-div">
        </div>
        <div class="text-div">
          <p>
            This project came to me from one of my coworkers. I was finishing up a project and wanted some new ideas 
            I spent time going through Kaggle's data sets and found some that were interesting to me. At about the 
            same time, at work, I was speaking with my coworker about Everest. She's very interested in the mountain and 
            we started talking about all the deaths on it. I happened to pull up a wikipedia page on Everest and it had data 
            on the amount of people who died there. I then told my coworker that I had an idea for my next project! 
          </p>
        </div>
      </div>
    </div>
</template>

<script>

</script>

<style scoped>
.main-div {
  display: grid;
  /* grid-template-columns: 1fr 1fr; */
  grid-template-columns: 60% 40%;
}

.pic-div {
  background: url("../../assets/images/Everest_line.jpg") center/cover no-repeat;
  height: 800px;
  margin-right: 5%;
}
</style>