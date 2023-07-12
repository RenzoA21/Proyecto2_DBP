<template>
  <div>
    <nav class="navbar">
      <ul>
        <li><a href="/frontend/src/views/CreationView.vue">Inicio</a></li>
        <li><a href="/frontend/src/views/LoginView.vue">Login</a></li>
        <li><a href="/frontend/src/views/RecetaView.vue">Receta</a></li>
        <li><a href="/frontend/src/views/DeliveryView.vue">Delivery</a></li>
      </ul>
    </nav>

    <main>
      <h1>Bienvenido a nuestro sitio web!</h1>

      <carousel :perPage="3">
        <slide
          ><img src="/frontend/src/assets/slideshow1.png" alt="slideshow1"
        /></slide>
        <slide
          ><img src="/frontend/src/assets/slideshow2.png" alt="slideshow1"
        /></slide>
        <slide
          ><img src="/frontend/src/assets/slideshow3.png" alt="slideshow3"
        /></slide>
      </carousel>
    </main>
  </div>
</template>

<script>
import { Carousel, Slide } from "vue-carousel";

export default {
  name: "CreationView",
  components: {
    Carousel,
    Slide,
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
}

.navbar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
}

.navbar li {
  float: left;
}

.navbar a {
  display: block;
  color: white;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
}

.navbar a:hover {
  background-color: #ddd;
  color: black;
}

.carousel {
  margin-top: 20px;
}

.slide img {
  width: 100%;
  height: auto;
}
</style>
