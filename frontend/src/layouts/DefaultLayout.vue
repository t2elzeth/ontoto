<template>
  <Navbar />
  <main class="main">
    <slot />
  </main>
</template>

<script>
import Navbar from "@/components/layout/Navbar";

export default {
  name: "DefaultLayout",
  components: {
    Navbar
  }
};
</script>

<style scoped></style>
