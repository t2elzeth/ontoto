import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { VuelidatePlugin } from "@vuelidate/core";

import DefaultLayout from "@/layouts/DefaultLayout";

const app = createApp(App);

app.use(router);
app.use(VuelidatePlugin);

app.component("default-layout", DefaultLayout);

app.mount("#app");
