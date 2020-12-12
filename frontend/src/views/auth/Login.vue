<template>
  <div class="main">
    <form @submit.prevent="login">
      <div class="container">
        <h1>Login</h1>
        <p>Please fill in this form to login into your account.</p>
        <hr/>

        <FormField
            :v$field="v$.email"
            placeholder="Enter email"
            label-text="Email"
            form-field="email"
        />
        <FormField
            :v$field="v$.password"
            placeholder="Enter password"
            label-text="Password"
            input-type="password"
            form-field="password"
        />
        <button type="submit" class="register-btn">Login</button>
      </div>

      <div class="container signin">
        <p>Don't have an account yet? <a href="#">Sign up</a>.</p>
      </div>
    </form>
    <button @click="whoAmI" class="register-btn">
      WhoAmI
    </button>
  </div>
</template>

<script>
import FormField from "@/components/FormField";

import axios from "axios";

import {useVuelidate} from "@vuelidate/core";

import {success, error} from "@/utils/notifications";
import {urls} from "@/utils/api";
import {auth} from "@/utils/auth";
import {formData} from "@/utils/forms";
import {rules} from "@/utils/validation";

export default {
  name: "Login",
  components: {
    FormField
  },
  setup() {
    let loginFormData = formData.login;

    const v$ = useVuelidate(rules.login(), loginFormData);

    function login() {
      // Validate data
      v$.value.$touch();
      // If it is still invalid, notify user
      if (v$.value.$invalid) return error("Your data is invalid");

      // If data is valid
      success("You were logged in successfully").finally(() =>
          location.reload()
      );

      // axios
      //   .post(urls.login, { email, password })
      //   .then(res => auth.setCredentials(res.data.auth_token))
      //   .catch(err => console.log(err));
    }

    function whoAmI() {
      // axios
      //   .get(urls.whoAmI, auth.getCredentials())
      //   .then(res => console.log(res.data))
      //   .catch(err => console.log(err));
    }

    function logout() {
      axios.post(urls.logout, {}, auth.getCredentials());
      auth.removeToken();
    }

    return {
      login,
      logout,
      whoAmI,
      v$,
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
