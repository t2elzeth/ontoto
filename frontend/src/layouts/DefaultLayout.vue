<template>
  <Navbar />
  <main class="main">
    <slot />
  </main>
  <Footer />
</template>

<script>
import Navbar from "@/components/layout/Navbar";
import Footer from "@/components/layout/Footer";

export default {
  name: "DefaultLayout",
  components: {
    Navbar,
    Footer
  }
};
</script>

<style scoped></style>
