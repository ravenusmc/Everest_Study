<template>
  <div class="signup-container">
    <div class="signup-box">
      <h1 class="signup-title">Sign Up</h1>

      <form class="signup-form" @submit.prevent="handleSubmit">
        <label>Username</label>
        <input v-model="form.username" type="text" placeholder="Enter your username" required />

        <label>First Name</label>
        <input v-model="form.firstName" type="text" placeholder="First name" required />

        <label>Last Name</label>
        <input v-model="form.lastName" type="text" placeholder="Last name" required />

        <label>Email</label>
        <input v-model="form.email" type="email" placeholder="you@example.com" required />

        <label>Password</label>
        <input v-model="form.password" type="password" placeholder="Enter password" required />

        <label>Verify Password</label>
        <input v-model="form.verifyPassword" type="password" placeholder="Re-enter password" required />

        <button type="submit" class="signup-btn">Create Account</button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "SignUpPage",
  data() {
    return {
      form: {
        username: "",
        firstName: "",
        lastName: "",
        email: "",
        password: "",
        verifyPassword: "",
      },
    };
  },
  methods: {
    ...mapActions("user", ["signUpUser"]),
    handleSubmit() {
      if (this.form.password !== this.form.verifyPassword) {
        alert("Passwords do not match!");
        return;
      }
      const payload = {
        username: this.username,
        firstName: this.firstName,
        lastName: this.lastName,
        email: this.email,
        password: this.password,
      };
      console.log("Form submitted:", this.form);
      this.signUpUser({ payload });
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
</style>
