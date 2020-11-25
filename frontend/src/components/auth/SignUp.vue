<template>
  <div class="app">
    <form action="" class="form" @submit.prevent="submitForm">
      <div class="form-field">
        <label for="id_email">Почта</label>
        <input type="text" id="id_email" v-model="formData.email" />
      </div>

      <div class="form-field">
        <label for="id_full_name">Полное имя</label>
        <input type="text" id="id_full_name" v-model="formData.full_name" />
      </div>

      <div class="form-field">
        <label for="id_phone">Номер телефона</label>
        <input type="text" id="id_phone" v-model="formData.phone" />
      </div>

      <div class="form-field">
        <label for="id_password">Пароль</label>
        <input type="password" id="id_password" v-model="formData.password" />
      </div>

      <div class="form-field">
        <label for="id_password2">Повторите пароль</label>
        <input type="password" id="id_password2" v-model="formData.password2" />
      </div>

      <div class="form-field">
        <label for="id_description">Описание для вашего профиля</label>
        <input type="text" id="id_description" v-model="formData.description" />
      </div>

      <input type="submit" value="Sign up" />
    </form>
  </div>
</template>

<script>
import axios from "axios";
// import { ref } from "vue";

const urls = {
  signUpUrl: "http://127.0.0.1:8001/api/auth/users/"
};

export default {
  name: "SignUp",
  setup() {
    const formData = {
      email: "",
      full_name: "",
      phone: "",
      password: "",
      password2: "",
      description: ""
    };

    function submitForm() {
      console.log("FORM HAS BEEN SUBMITTED");

      axios
        .post(urls.signUpUrl, formData)
        .then(res => {
          console.log(res.data);
        })
        .catch(err => {
          console.log(err);
        });
    }

    return {
      formData,
      submitForm
    };
  }
};
</script>

<style scoped>
.app {
  display: flex;
  justify-content: center;
  width: 100%;
}

.form {
  width: 30%;
}

.form-field {
  display: flex;
  justify-content: space-between;
}
</style>
