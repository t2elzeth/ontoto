<template>
  <div class="main">
    <div class="container">
      <FormHeader focus-on="signup" />
      <form @submit.prevent="signUp" class="form">
        <FormField
          :v$field="v$.username"
          placeholder="имя пользователя"
          form-field="username"
        />
        <FormField :v$field="v$.email" placeholder="email" form-field="email" />
        <FormField
          :v$field="v$.password"
          placeholder="пароль"
          input-type="password"
          form-field="password"
        />
        <FormField
          :v$field="v$.password2"
          placeholder="повторите пароль"
          input-type="password"
          form-field="password2"
        />
        <p class="agreement">
          Регистрируясь, вы принимаете наши
          <a href="#">условия конфиденциальности</a> и
          <a href="#">политику в отношении файлов cookie.</a>
        </p>
        <button type="submit" class="register-btn">регистрация</button>
      </form>
    </div>
  </div>
</template>

<script>
import FormField from "@/components/form/FormField";
import FormHeader from "@/components/form/FormHeader";

import axios from "axios";
import { useVuelidate } from "@vuelidate/core";

import { success, error } from "@/utils/notifications";
import { formData } from "@/utils/forms/forms";
import { rules as globalRules } from "@/utils/forms/validation";
import { urls } from "@/utils/api";
import { setTitle } from "@/utils/layouts";

export default {
  name: "SignUp",
  components: {
    FormHeader,
    FormField
  },
  setup() {
    setTitle("Регистрация");

    const signUpFormData = formData.signUp;
    const rules = {
      username: globalRules.username,
      email: globalRules.email,
      password: globalRules.password,
      password2: globalRules.password2(signUpFormData.password)
    };
    const v$ = useVuelidate(rules, signUpFormData);

    // axios
    //   .post(urls.signUp, signUpFormData)
    //   .then(res => console.log(res.data))
    //   .catch(err => console.log(err));

    function signUp() {
      // Validate data
      v$.value.$touch();
      // If data is invalid
      if (v$.value.$invalid)
        return error("Введенные данные не корректны!", "Ошибка!");

      axios
        .post(urls.signUp, {
          username: signUpFormData.username.value,
          email: signUpFormData.email.value,
          password: signUpFormData.password.value,
          password2: signUpFormData.password2.value
        })
        .then(() => {
          success("Your account has been successfully created");
        })
        .catch(() => {
          error("Server error!");
        });
    }

    return {
      signUp,
      v$
    };
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/forms";
.main {
  .container {
    .form {
      margin-top: 0;
    }
  }
}
</style>
