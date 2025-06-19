<template>
  <section class="about">
    <div class="content">
      <div class="image"></div>
      <div class="text">
        <p>
          This project came to me from one of my coworkers. I was finishing up a project and wanted some new ideas.
          I spent time going through Kaggle's datasets and found some that were interesting to me. Around the same time,
          at work, I was speaking with my coworker about Everest. She's very interested in the mountain, and
          we started talking about all the deaths on it. I happened to pull up a Wikipedia page on Everest and it had data 
          on the number of people who died there. I then told my coworker that I had an idea for my next project!
        </p>
        <p>
          Like my other projects, I work with a dataset and build graphs so people can visualize the data.
          I think there will be some basic graphs — like the top 5 states where people came from who died,
          and the top 5 reasons for deaths. The dataset has about 346 entries.
          I don't know if that's enough to do more complex analysis. I’ll ask ChatGPT about that!
        </p>
        <p>
          Finally, how did I get the data? As I said, it comes from a Wikipedia page.
          I webscraped that page and saved the data to a CSV file, which I then used for analysis.
        </p>
      </div>
    </div>
  </section>
</template>


<script>

</script>

<style scoped>
.about {
  padding: 2rem;
  background: #121212; /* deep dark background */
  border-radius: 8px;
  color: #e0e0e0; /* light text for contrast */
  margin-bottom: 50px;
}

.content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2rem;
  align-items: start;
}

.image {
  background: url("../../assets/images/Everest_line.jpg") center/cover no-repeat;
  min-height: 400px;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
}

.text {
  font-size: 1.1rem;
  line-height: 1.8rem;
  background: #1e1e1e; /* slightly lighter than outer background */
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
}

.text p {
  margin-bottom: 1rem;
}

@media (max-width: 900px) {
  .content {
    grid-template-columns: 1fr;
  }
  
  .image {
    min-height: 300px;
  }
}
</style>

