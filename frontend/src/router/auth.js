export const authRoutes = [
  {
    path: "/signup",
    name: "SignUp",
    meta: {
      layout: "default-layout"
    },
    component: () => import("@/views/auth/SignUp")
  },
  {
    path: "/login",
    name: "Login",
    meta: {
      layout: "default-layout"
    },
    component: () => import("@/views/auth/Login")
  }
];
