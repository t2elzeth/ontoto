<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="login">
      <div class="container">
        <h1>Login</h1>
        <p>Please fill in this form to login into your account.</p>
        <hr />

        <FormField
          id="email"
          :v$field="v$.email"
          placeholder="Enter email"
          label-text="Email"
          :validators="[getValidator.required('Email'), getValidator.email()]"
        />
        <FormField
          :v$field="v$.password"
          id="password"
          placeholder="Enter password"
          label-text="Password"
          input-type="password"
          :validators="[
            getValidator.required('Password'),
            getValidator.minLength('Password', 'password')
          ]"
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
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import FormField from "@/components/FormField";

import axios from "axios";

import { useVuelidate } from "@vuelidate/core";
import { required, minLength, email } from "@vuelidate/validators";

import { success, error } from "@/utils/notifications";
import { urls } from "@/utils/api";
import { auth } from "@/utils/auth";
import {
  getInputFieldValidationClasses,
  validators,
  getValidator,
  formData
} from "@/utils/forms";

export default {
  name: "Login",
  components: {
    Navbar,
    Sidebar,
    FormField
  },
  setup() {
    let loginFormData = formData.login;

    const rules = {
      email: {
        email,
        required
      },
      password: {
        required,
        minLength: minLength(validators.minLength.password)
      }
    };

    const v$ = useVuelidate(rules, loginFormData);

    function login() {
      // Validate data
      v$.value.$touch();

      // If it is still invalid, notify user
      if (v$.value.$invalid) {
        error("Your data is invalid");
        return;
      }

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

      console.log(loginFormData.email.value);
      console.log(loginFormData.password.value);
      // console.log(v$.value.password.$model);
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
      getInputFieldValidationClasses,
      loginFormData,
      validators,
      getValidator
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
