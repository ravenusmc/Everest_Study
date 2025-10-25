<template>
  <div>
    <nav class="navbar">
      <div class="navlinks-left">
        <router-link class="navlink link-style" to="/">Home</router-link>
        <router-link class="navlink link-style" to="/data">Data</router-link>
        <router-link class="navlink link-style" to="/about">About</router-link>
      </div>
      <div class="navlinks-right">
        <router-link v-if="!loginFlag" class="navlink link-style" to="/login">Login</router-link>
        <router-link v-if="!loginFlag" class="navlink link-style" to="/signup">Sign Up</router-link>
        <a v-if="loginFlag" @click.prevent="logoutUser"><router-link  class="navlink link-style" to="/">Log Out</router-link></a>
      </div>
    </nav>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "NavBar",
  computed: {
    ...mapGetters("user", ["passwordNoMatch", "loginFlag"]),
  },
  methods: {
  ...mapActions("user", ["logout"]),
  logoutUser: function () {
    this.logout();
    },
  },
}
</script>

<style scoped>

.navbar {
  background-color: #121212;
  height: 50px;
  display: flex; 
  justify-content: space-between;
  align-items: center;
  padding: 0 15px;
  position: relative;
  z-index: 9999;
  pointer-events: auto;
}

.link-style {
  color: white;
  text-decoration: none;
}

.navlink {
  font-size: 1.5rem;
  margin: 10px 15px;
}

.navlinks-left,
.navlinks-right {
  display: flex;
  align-items: center;
}
</style>
