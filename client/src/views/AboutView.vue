<template>
  <section class="about">
    <!-- Header -->
    <header class="about-header">
      <h1 class="title">My Story</h1>
    </header>

    <!-- Content -->
    <div class="content">
      <div class="image"></div>

      <div class="bio">
        <p>
          In the spring of 2015, I chose to take a leap in a new direction and
          immerse myself in learning full stack web development. I attended the
          coding bootcamp Tech Talent South as well as Gwinnett Technical
          College for a degree in web development. Since then, I have fully
          immersed myself in the Atlanta tech community, attending meetups,
          conferences, and hackathons to grow as a developer. I’ve won
          first place two years in a row at the SkillsUSA state level in web
          design and competed at the national level. I’ve worked with Manning
          Publications to review many of their books and videos on the latest
          technology trends. I continue to stay up to date with the
          latest technologies using resources like Team Treehouse and
          Udemy. My casual interest in web development has become a guiding
          passion, and I am excited to bring that passion to my next pursuit.
        </p>

        <p>
          The experience I gained in the Marine Corps and C.I.A. has
          given me the confidence and ability to succeed in any field. I’ve
          proven my ability to work well under pressure when I had three months
          to prepare 40 Marines for deployment to Camp Fallujah, Iraq. I’ve
          demonstrated strong communication skills writing a new convoy
          operations manual for my unit in Afghanistan and delivering 79 convoy
          briefs in Iraq. My planning skills were proven when I coordinated 15 convoys
          across South Korea, moving over 1,000 pieces of decking, tents, and aircraft equipment.
        </p>

        <p>
          Feel free to send me an invite — I’d love to connect with you.
        </p>
      </div>
    </div>
  </section>
</template>

  
<script>
export default {
  name: 'AboutView',
}
</script>
  
<style scoped>
/* General section styling */
.about {
  padding: 2rem;
  background: #121212; /* deep dark background */
  color: #e0e0e0; /* soft light text */
  border-radius: 8px;
  margin: 75px;
  flex: 1; /* important! allows it to grow and push footer down */
  display: flex;
  flex-direction: column;
}

/* Header styling */
.about-header {
  text-align: center;
  margin-bottom: 2rem;
}

.title {
  text-transform: uppercase;
  font-size: 2rem;
  letter-spacing: 2px;
  color: #ffffff;
}

/* Content layout */
.content {
  display: grid;
  grid-template-columns: 300px 1fr;
  gap: 2rem;
  align-items: start;
}

/* Profile image */
.image {
  width: 100%;
  height: 400px;
  border-radius: 10px;
  background: url("../assets/images/Cuddy.jpg") center/cover no-repeat;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7);
}

/* Bio text block */
.bio {
  background: #1e1e1e;
  padding: 1.5rem;
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6);
  font-size: 1.1rem;
  line-height: 1.8rem;
}

.bio p {
  margin-bottom: 1rem;
}

/* Responsive for mobile */
@media (max-width: 900px) {
  .content {
    grid-template-columns: 1fr;
  }

  .image {
    height: 300px;
  }
}
</style>
