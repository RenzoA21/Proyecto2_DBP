<template>
  <div id="app">
    <nav class="navbar">
      <ul>
        <li><router-link to="/">Inicio</router-link></li>
        <li><router-link to="/login">Login</router-link></li>
        <li><router-link to="/Receta">Receta</router-link></li>
        <li><router-link to="/delivery">Delivery</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

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

.navbar a.router-link-exact-active {
  color: #42b983;
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

  .navbar a {
    margin: 5px 0;
  }
}
</style>
