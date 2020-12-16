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
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
}
</style>
