import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home";
import SignUpView from "@/views/auth/SignUp";
import LoginView from "@/views/auth/Login";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue")
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignUpView
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
