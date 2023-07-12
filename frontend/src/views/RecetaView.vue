<template>
  <div class="form-container">
    <h1>Por favor ingresa los datos de la receta</h1>
    <form>
      <input type="text" placeholder="Tipo" />
      <input type="text" placeholder="Medida" />
      <input type="text" placeholder="Unidad de medida" />
      <input type="text" placeholder="Cantidad" />
      <button type="submit">Enviar</button>
    </form>
  </div>
</template>

<script>
export default {
  name: "RecetaView",
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
