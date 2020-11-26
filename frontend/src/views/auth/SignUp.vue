<template>
  <div class="app">
    <form action="" class="form" @submit.prevent="signUp">
      <div class="form-field">
        <label for="id_email">Почта</label>
        <input type="text" id="id_email" v-model="signUpFormData.email" />
      </div>

      <div class="form-field">
        <label for="id_full_name">Полное имя</label>
        <input
          type="text"
          id="id_full_name"
          v-model="signUpFormData.full_name"
        />
      </div>

      <div class="form-field">
        <label for="id_phone">Номер телефона</label>
        <input type="text" id="id_phone" v-model="signUpFormData.phone" />
      </div>

      <div class="form-field">
        <label for="id_password">Пароль</label>
        <input
          type="password"
          id="id_password"
          v-model="signUpFormData.password"
        />
      </div>

      <div class="form-field">
        <label for="id_password2">Повторите пароль</label>
        <input
          type="password"
          id="id_password2"
          v-model="signUpFormData.password2"
        />
      </div>

      <div class="form-field">
        <label for="id_description">Описание для вашего профиля</label>
        <input
          type="text"
          id="id_description"
          v-model="signUpFormData.description"
        />
      </div>

      <input type="submit" value="Sign up" />
    </form>
  </div>
</template>

<script>
import axios from "axios";
// import { ref } from "vue";
import { urls, auth } from "@/utils/api";

export default {
  name: "SignUp",
  setup() {
    const signUpFormData = auth.formData.signUp;

    function signUp() {
      console.log("FORM HAS BEEN SUBMITTED");
      axios
        .post(urls.signUp, signUpFormData)
        .then(res => console.log(res.data))
        .catch(err => console.log(err));
    }

    return {
      signUpFormData,
      signUp
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
</style>
