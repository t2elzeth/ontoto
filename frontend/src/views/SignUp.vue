<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png"/>
    <SignUp msg="Welcome to Your Vue.js App"/>
  </div>
</template>

<script>
import SignUp from "@/components/auth/SignUp.vue";

export default {
  name: "SignUp",
  components: {
    SignUp
  },
};
</script>
