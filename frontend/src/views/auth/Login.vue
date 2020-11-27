<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form action="" class="form" @submit.prevent="login">
      <div class="form-field">
        <label for="id_email">Почта</label>
        <input type="text" id="id_email" v-model="loginFormData.email" />
      </div>

      <div class="form-field">
        <label for="id_password">Пароль</label>
        <input
          type="password"
          id="id_password"
          v-model="loginFormData.password"
        />
      </div>

      <input type="submit" value="Sign up" />
    </form>
    <button @click="whoAmI">WhoAmI</button>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";

import axios from "axios";

import { urls, auth } from "@/utils/api";

export default {
  name: "Login",
  components: {
    Navbar,
    Sidebar
  },
  setup() {
    const loginFormData = auth.formData.login;

    function login() {
      console.log(loginFormData);
      axios
        .post(urls.login, loginFormData)
        .then(res => auth.setCredentials(res.data.auth_token))
        .catch(err => console.log(err));
    }

    function whoAmI() {
      axios
        .get(urls.whoAmI, auth.getCredentials())
        .then(res => console.log(res.data))
        .catch(err => console.log(err));

      console.log(auth.getToken());
    }

    function logout() {
      axios.post(urls.logout, {}, auth.getCredentials());
      auth.removeToken();
    }

    return {
      loginFormData,
      login,
      logout,
      whoAmI
    };
  }
};
</script>

<style scoped lang="scss">
.app {
  display: flex;
  justify-content: center;
  width: 100%;

  .form {
    width: 30%;

    &-field {
      display: flex;
      justify-content: space-between;
    }
  }
}

.main {
  margin-left: 160px; /* Same as the width of the sidebar */

  display: flex;
  flex-direction: column;
  justify-content: center;
}
</style>
