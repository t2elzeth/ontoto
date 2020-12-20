<template>
  <div class="main">
    <div class="container">
      <FormHeader focus-on="login" />
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
      <button @click="whoAmI">CLICK ME HARD</button>
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
import { formData } from "@/utils/forms/forms";
import { rules as globalRules } from "@/utils/forms/validation";
import { setTitle } from "@/utils/layouts";

export default {
  name: "Login",
  components: {
    FormField,
    FormHeader
  },
  setup() {
    setTitle("Войти");

    const loginFormData = formData.login;
    const rules = {
      email: globalRules.email,
      password: globalRules.password
    };
    const v$ = useVuelidate(rules, loginFormData);

    function login() {
      // Validate data
      v$.value.$touch();
      // If it is still invalid, notify user
      if (v$.value.$invalid) return error("Your data is invalid");

      // If data is valid
      axios
        .post(urls.login, {
          email: loginFormData.email.value,
          password: loginFormData.password.value
        })
        .then(res => {
          success("You were logged in successfully").finally(() =>
            location.reload()
          );

          auth.setCredentials(res.data);
        })
        .catch(() => error("Internal server error!"));
    }

    function logout() {
      if (!auth.isAuthenticated())
        return error("Вы уже вышли!", "Ошибка!").finally(() =>
          location.reload()
        );
      axios.post(urls.logout, {}, auth.getCredentials());
      auth.removeToken();
    }

    function whoAmI() {
      // axios
      //   .post("http://127.0.0.1:8000/pay/elsom/", data, { contentType: 'application/xml' })
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
