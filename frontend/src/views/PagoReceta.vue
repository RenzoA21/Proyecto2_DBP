<template>
  <div id="app">
    <nav class="menu">
      <router-link to="/login">Login</router-link>
      <router-link to="/Receta">Receta</router-link>
      <router-link to="/delivery">Delivery</router-link>
      <router-link to="/Preceta">Preceta</router-link>
      <router-link to="/Pdelivery">Pdelivery</router-link>
    </nav>

    <div class="content">
      <table class="recetas">
        <thead>
          <tr>
            <th>Receta</th>
            <th>Ingredientes</th>
            <th>Procedimiento</th>
          </tr>
        </thead>
        <tbody>
          <!-- Debes llenar las filas de la tabla dinámicamente con los datos de tus recetas -->
          <tr>
            <td>Receta 1</td>
            <td>Ingredientes 1</td>
            <td>Procedimiento 1</td>
          </tr>
          <!-- Más filas según sea necesario -->
        </tbody>
      </table>

      <img
        class="side-image"
        src="../assets/slideshow1.png"
        alt="Descripción de la imagen"
      />
    </div>
  </div>
</template>

<style>
/* ... estilos del menú ... */

.content {
  display: flex;
  justify-content: space-between;
  padding: 20px;
}

.recetas {
  width: 70%;
  border-collapse: collapse;
}

.recetas th,
.recetas td {
  border: 1px solid #ddd;
  padding: 8px;
}

.side-image {
  max-width: 25%;
  height: auto;
  align-self: center;
}

@media (max-width: 600px) {
  .content {
    flex-direction: column;
    align-items: center;
  }

  .recetas {
    width: 100%;
  }

  .side-image {
    max-width: 100%;
    margin-top: 20px;
  }
}
</style>
