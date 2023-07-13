<template>
  <div class="container">
    <form @submit.prevent="submitForm" class="login-form">
      <h2>Login</h2>

      <div class="input-group">
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" required />
      </div>

      <div class="input-group">
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" required />
      </div>

      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://127.0.0.1:5002", {
          username: this.email,
          password: this.password,
        });
        if (response.data.msg === "credenciales correctas") {
          this.$router.push("/home");
        } else {
          console.log("Error de inicio de sesión: ", response.data.msg);
        }
      } catch (error) {
        console.error("Ocurrió un error:", error);
      }
    },
  },
};
</script>

<style scoped>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  gap: 20px;
  padding: 40px;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #fff;
  width: 50%;
  max-width: 500px;
}

.input-group {
  display: flex;
  flex-direction: column;
}

.input-group label {
  text-align: left;
}

input {
  padding: 10px;
  border-radius: 3px;
  border: 1px solid #ccc;
  font-size: 16px;
}

button {
  padding: 10px 20px;
  border-radius: 3px;
  border: none;
  color: #fff;
  background-color: #007bff;
  cursor: pointer;
  font-size: 18px;
}

button:hover {
  background-color: #0056b3;
}
</style>
