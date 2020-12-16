<template>
  <div class="main">
    <div class="container">
      <FormHeader />
      <form @submit.prevent="login" class="form">
        <FormField
          :v$field="v$.email"
          placeholder="введите email"
          form-field="email"
        />
        <FormField
          :v$field="v$.password"
          placeholder="пароль"
          input-type="password"
          form-field="password"
        />
        <button type="submit" class="register-btn">войти</button>
      </form>
      <a href="#" class="get-help">забыли пароль?</a>
      <!--      <button @click="whoAmI">CLICK ME HARD</button>-->
    </div>
  </div>
</template>

<script>
import FormField from "@/components/form/FormField";
import FormHeader from "@/components/form/FormHeader";

import axios from "axios";

import { useVuelidate } from "@vuelidate/core";

import { success, error } from "@/utils/notifications";
import { urls } from "@/utils/api";
import { auth } from "@/utils/auth";
import { formData } from "@/utils/forms";
import { rules } from "@/utils/validation";

export default {
  name: "Login",
  components: {
    FormField,
    FormHeader
  },
  setup() {
    const loginFormData = formData.login,
      v$ = useVuelidate(rules.login(), loginFormData);

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
    function logout() {
      axios.post(urls.logout, {}, auth.getCredentials());
      auth.removeToken();
    }

    function whoAmI() {
      // axios
      //   .get(urls.whoAmI, auth.getCredentials())
      //   .then(res => console.log(res.data))
      //   .catch(err => console.log(err));
      console.log("Salam");
    }

    return {
      login,
      logout,
      whoAmI,
      v$
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
.form-field {
  margin-bottom: 30px;
}
</style>
