<template>
  <component :is="layout">
    <router-view/>
  </component>
</template>

<script>
import {computed} from "vue";
import {useRoute} from "vue-router";

export default {
  name: "App",
  setup() {
    const defaultLayout = "default"
    const route = useRoute()

    const layout = computed(() => {
      return route.meta.layout || defaultLayout
    })

    return {
      layout
    }
  }
}

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
