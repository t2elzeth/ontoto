<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="login">
      <div class="container">
        <h1>Login</h1>
        <p>Please fill in this form to login into your account.</p>
        <hr />

        <FormField :field="loginFormData.email" :v$field="v$.email" />
        <FormField :field="loginFormData.password" :v$field="v$.password" />

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

import { ref } from "vue";
import axios from "axios";

import { useVuelidate } from "@vuelidate/core";
import { required, minLength, email } from "@vuelidate/validators";

import { success, error } from "@/utils/notifications";
import { urls } from "@/utils/api";
import { auth } from "@/utils/auth";
import {
  getInputFieldValidationClasses,
  validators,
  getStates
} from "@/utils/forms";

export default {
  name: "Login",
  components: {
    Navbar,
    Sidebar,
    FormField
  },
  setup() {
    const loginFormData = {
      email: {
        data: ref(""),
        id: "email",
        placeholder: "Enter email",
        labelText: "Email",
        validators: [
          {
            name: "required",
            message: "Email cannot be blank"
          },
          {
            name: "email",
            message: "Enter a valid email"
          }
        ]
      },
      password: {
        data: ref(""),
        id: "password",
        placeholder: "Enter Password",
        labelText: "Password",
        type: "password",
        validators: [
          {
            name: "required",
            message: "Password cannot be blank"
          },
          {
            name: "minLength",
            message: `Password must be at least ${validators.minLength.password} characters long`
          }
        ]
      }
    };

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

    const v$ = useVuelidate(rules, getStates(loginFormData));

    function login() {
      // Validate data
      v$.value.$touch();

      // If it is still invalid, notify user
      if (v$.value.$invalid) {
        error("Your data is invalid");
        return;
      }

      // If data is valid
      success("You were logged in successfully");
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

      console.log(loginFormData.email.data.value);
      console.log(loginFormData.password.data.value);
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
      loginFormData
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
