import { createRouter, createWebHistory } from "vue-router";

import { authRoutes } from "@/router/auth";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("@/views/Home")
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/views/About")
  },
  ...authRoutes
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
