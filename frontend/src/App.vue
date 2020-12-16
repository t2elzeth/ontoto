<template>
  <component :is="layout">
    <router-view />
  </component>
</template>

<script>
import { getLayout } from "@/utils/layouts";
import { useRoute } from "vue-router";

export default {
  name: "App",
  setup() {
    return {
      layout: getLayout(useRoute())
    };
  }
};
</script>

<style>
#app {
  font-family: "Poppins", Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
