<template>
  <div class="form-container">
    <h1>Por favor ingresa los datos de la receta</h1>
    <form @submit.prevent="submitForm">
      <input type="text" v-model="medicamento" placeholder="medicamento" />
      <input type="text" v-model="tipo_de_toma" placeholder="tipo_de_toma" />
      <input type="text" v-model="cantidad" placeholder="cantidad" />
      <input type="text" v-model="unidad_medida" placeholder="unidad_medida" />
      <input type="text" v-model="porcentaje" placeholder="porcentaje" />
      <input type="text" v-model="ml_g" placeholder="ml_g" />
      <button type="submit">Enviar</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RecetaView",
  data() {
    return {
      medicamento: "",
      tipo_de_toma: "",
      cantidad: "",
      unidad_medida: "",
      porcentaje: "",
      ml_g: "",
    };
  },
  methods: {
    async submitForm() {
      try {
        const response = await axios.post("http://127.0.0.1:5002/", {
          medicamento: this.medicamento,
          tipo_de_toma: this.tipo_de_toma,
          cantidad: this.cantidad,
          unidad_medida: this.unidad_medida,
          porcentaje: this.porcentaje,
          ml_g: this.ml_g,
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
.navbar {
  background-color: #333;
  overflow: hidden;
  position: fixed;
  top: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-around;
  width: 100%;
}

.navbar li {
  flex: 1;
  text-align: center;
}

.navbar a {
  display: block;
  color: white;
  text-decoration: none;
  padding: 14px 16px;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}

@media (max-width: 600px) {
  .navbar {
    flex-direction: column;
  }

  .navbar ul {
    flex-direction: column;
    align-items: center;
  }

  .navbar li {
    flex: none;
  }
}

.main {
  display: flex;
  justify-content: center;
  align-items: center;
  height: calc(100vh - 56px);
  padding-top: 56px;
}

.form-container {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  padding: 1em;
  width: 40%;
  max-width: 500px;
  margin: 250px auto 0 auto;
}

form {
  display: flex;
  flex-direction: column;
}

form input {
  margin-bottom: 1em;
  padding: 0.5em;
  font-size: 1em;
}

form button {
  padding: 0.5em 1em;
  font-size: 1em;
  color: #fff;
  background-color: #42b983;
  border: none;
  cursor: pointer;
}

form button:hover {
  background-color: #2c3e50;
}
</style>
