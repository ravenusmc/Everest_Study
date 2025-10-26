<template>
  <div class="signup-container">
    <div class="signup-box">
      <h1 class="signup-title">Login</h1>

      <form class="signup-form" @submit.prevent="handleLogin">
        <label>Username</label>
        <input v-model="form.username" type="text" placeholder="Enter your username" required />

        <label>Password</label>
        <input v-model="form.password" type="password" placeholder="Enter password" required />
        <p v-if="passwordNoMatch">Password Wrong</p>

        <button type="submit" class="signup-btn">Login</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "SignUpPage",
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
   computed: {
    ...mapGetters("user", ["passwordNoMatch", "loginFlag"]),
  },
  methods: {
    ...mapActions("user", ["loginUser"]),
    handleLogin() {
      const payload = {
        username: this.form.username,
        password: this.form.password,
      };
      this.loginUser({ payload });
    },
  },
};
</script>

<style scoped>
/* Container to center everything */
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  height: 100dvh; /* modern browsers will prefer this */
  background: linear-gradient(to right, #e0eafc, #cfdef3);
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
}

/* White box for the form */
.signup-box {
  background: white;
  padding: 2.5rem;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0, 0, 0, 0.1);
  width: 440px;
}

/* Title */
.signup-title {
  text-align: center;
  font-size: 1.8rem;
  color: #333;
  margin-bottom: 1.5rem;
  letter-spacing: 0.5px;
}

/* Form */
.signup-form {
  display: flex;
  flex-direction: column;
}

.signup-form label {
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 5px;
}

.signup-form input {
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.2s ease, box-shadow 0.2s ease;
}

.signup-form input:focus {
  border-color: #5b8def;
  box-shadow: 0 0 4px rgba(91, 141, 239, 0.4);
  outline: none;
}

/* Name fields side by side */
.name-row {
  display: flex;
  gap: 10px;
}

.name-field {
  flex: 1;
}

/* Button */
.signup-btn {
  background-color: #5b8def;
  color: white;
  border: none;
  padding: 12px;
  border-radius: 8px;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
}

.signup-btn:hover {
  background-color: #4a7bd8;
}

.signup-btn:active {
  transform: scale(0.98);
}

p {
  color: red;
  text-transform: uppercase;
}
</style>
