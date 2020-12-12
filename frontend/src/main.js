import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { VuelidatePlugin } from "@vuelidate/core";

import Default from "@/layouts/Default";

const app = createApp(App);

app.use(router);
app.use(VuelidatePlugin);

app.component("default", Default);

app.mount("#app");
