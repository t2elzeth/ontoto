export const authRoutes = [
  {
    path: "/signup",
    name: "SignUp",
    meta: {
      layout: "default"
    },
    component: () => import("@/views/auth/SignUp")
  },
  {
    path: "/login",
    name: "Login",
    meta: {
      layout: "default"
    },
    component: () => import("@/views/auth/Login")
  }
];
