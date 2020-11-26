import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import { VuelidatePlugin } from "@vuelidate/core";

// import axios from "axios";
// import VueAxios from "vue-axios";

const app = createApp(App);

app.use(router);
app.use(VuelidatePlugin);
app.mount("#app");
