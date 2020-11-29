import { createRouter, createWebHashHistory } from "vue-router";
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
    component: () => import("@/views/auth/SignUp")
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("@/views/auth/Login")
  },
  {
    path: "/test",
    name: "Test",
    component: () => import("@/views/Test")
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
