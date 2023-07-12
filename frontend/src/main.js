import { createApp } from "vue";
import App from "./App.vue";
import Carousel from "vue-carousel";
import router from "./router/index.js";

createApp(App).use(Carousel).use(router).mount("#app");
