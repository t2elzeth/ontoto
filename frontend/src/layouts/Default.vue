<template>
  <Navbar />
  <main class="main">
    <slot />
  </main>
</template>

<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "Default",
  components: {
    Navbar
  }
};
</script>

<style scoped></style>
