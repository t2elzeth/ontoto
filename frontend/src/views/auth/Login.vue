<template>
  <Navbar />
  <Sidebar />
  <div class="main">
    <form @submit.prevent="login">
      <div class="container">
        <h1>Login</h1>
        <p>Please fill in this form to login into your account.</p>
        <hr />

        <div class="form-field">
          <FieldLabel
            :label="getFieldLabelProps('email', 'Email', vuelidate.email)"
          />
          <input
            type="text"
            placeholder="Enter Email"
            v-model="vuelidate.email.$model"
            :class="getInputFieldValidationClasses(vuelidate.email)"
            id="email"
          />

          <ValidationMessages
            :field="vuelidate.email"
            :validators="[
              {
                name: 'required',
                message: 'Email cannot be blank'
              },
              {
                name: 'emailValidator',
                message: 'Enter a valid email'
              }
            ]"
          />
        </div>

        <div class="form-field">
          <FieldLabel
            :label="
              getFieldLabelProps('password', 'Password', vuelidate.password)
            "
          />
          <input
            type="password"
            placeholder="Enter Password"
            v-model="vuelidate.password.$model"
            :class="getInputFieldValidationClasses(vuelidate.password)"
            id="psw"
          />
          <ValidationMessages
            :field="vuelidate.password"
            :validators="[
              {
                name: 'required',
                message: 'Password cannot be blank'
              },
              {
                name: 'minLength',
                message: `Password must be at least ${validators.minLength.password} characters long`
              }
            ]"
          />
        </div>

        <button type="submit" class="register-btn">Login</button>
      </div>

      <div class="container signin">
        <p>Don't have an account yet? <a href="#">Sign up</a>.</p>
      </div>
    </form>
    <button @click="whoAmI" :disabled="vuelidate.$invalid" class="register-btn">
      WhoAmI
    </button>
  </div>
</template>

<script>
import Navbar from "@/components/Navbar";
import Sidebar from "@/components/Sidebar";
import ValidationMessages from "@/components/ValidationMessages";
import FieldLabel from "@/components/FieldLabel";

import { ref } from "vue";
import axios from "axios";

import { useVuelidate } from "@vuelidate/core";
import {
  required,
  minLength,
  email as emailValidator
} from "@vuelidate/validators";

import { notify } from "@/utils/use";
import { urls } from "@/utils/api";
import { auth } from "@/utils/auth";
import {
  getFieldLabelProps,
  getInputFieldValidationClasses,
  validators
} from "@/utils/forms";

export default {
  name: "Login",
  components: {
    Navbar,
    Sidebar,
    ValidationMessages,
    FieldLabel
  },
  setup() {
    const loginFormData = ref({
      email: "",
      password: ""
    });

    const rules = {
      email: {
        emailValidator,
        required
      },
      password: {
        required,
        minLength: minLength(validators.minLength.password)
      }
    };

    const vuelidate = useVuelidate(rules, loginFormData);

    function login() {
      vuelidate.value.$touch();

      if (vuelidate.value.$invalid) {
        console.log("DATA IS INVALID");
        return;
      }
      console.log("EVERYTHING IS OKAY");
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
      //
      // console.log(auth.getToken());

      console.log(notify);
    }

    function logout() {
      axios.post(urls.logout, {}, auth.getCredentials());
      auth.removeToken();
    }

    return {
      login,
      logout,
      whoAmI,
      vuelidate,
      getFieldLabelProps,
      getInputFieldValidationClasses,
      validators
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
</style>
