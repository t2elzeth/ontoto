import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    component: () => import("@/views/About")
  },
  {
    path: "/signup",
    name: "SignUp",
    meta: {
      layout: "default",
    },
    component: () => import("@/views/auth/SignUp")
  },
  {
    path: "/login",
    name: "Login",
    meta: {
      layout: "default",
    },
    component: () => import("@/views/auth/Login")
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;
