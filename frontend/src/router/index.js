import { createRouter, createWebHashHistory } from "vue-router";
import Home from "../views/Home.vue";
import SignUp from "@/components/auth/SignUp";

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
    path: '/signup',
    name: 'SignUp',
    component: SignUp
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

export default router;
