import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RecetaView from "@/views/RecetaView.vue";
import DeliveryView from "@/views/DeliveryView.vue";
import PagoReceta from "@/views/PagoReceta.vue";
import PagoDelivery from "@/views/PagoDelivery.vue";

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/receta",
    name: "Receta",
    component: RecetaView,
  },
  {
    path: "/delivery",
    name: "Delivery",
    component: DeliveryView,
  },
  {
    path: "/Preceta",
    name: "Preceta",
    component: PagoReceta,
  },
  {
    path: "/Pdelivery",
    name: "Pdelivery",
    component: PagoDelivery,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
