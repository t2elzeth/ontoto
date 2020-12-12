<template>
  <Navbar/>
  <Sidebar/>
  <main class="main">
    <slot/>
  </main>
</template>

<script>
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

export default {
  name: "Default",
  components: {
    Navbar, Sidebar
  }
}
</script>

<style scoped>

</style>