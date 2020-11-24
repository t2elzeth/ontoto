<template>
  <div class="app">
    <form action="" class="form" @submit.prevent="submitForm">
      <div class="form-field">
        <label for="id_email">Почта</label>
        <input type="text" id="id_email" v-model="email">
      </div>

      <div class="form-field">
        <label for="id_full_name">Полное имя</label>
        <input type="text" id="id_full_name" v-model="full_name">
      </div>

      <div class="form-field">
        <label for="id_phone">Номер телефона</label>
        <input type="text" id="id_phone" v-model="phone">
      </div>

      <div class="form-field">
        <label for="id_password">Пароль</label>
        <input type="password" id="id_password" v-model="password">
      </div>

      <div class="form-field">
        <label for="id_password2">Повторите пароль</label>
        <input type="password" id="id_password2" v-model="password2">
      </div>

      <div class="form-field">
        <label for="id_description">Описание для вашего профиля</label>
        <input type="text" id="id_description" v-model="description">
      </div>

      <input type="submit" value="Sign up">
    </form>
    {{ userData }}
  </div>
</template>


<script>
import axios from 'axios';

const urls = {
  signUpUrl: 'http://127.0.0.1:8001/api/auth/users/',
}

export default {
  name: 'SignUp',
  data() {
    return {
      msg: 'HelloWorld!',
      email: '',
      full_name: '',
      phone: '',
      password: '',
      password2: '',
      description: '',
      userData: {}
    }
  },
  created() {
    console.log('My VueJS app has been created')
  },
  methods: {
    submitForm() {
      console.log('FORM HAS BEEN SUBMITTED')

      axios.post(urls.signUpUrl, {
        full_name: this.full_name,
        email: this.email,
        phone: this.phone,
        description: this.description,
        password: this.password,
        password2: this.password2,
      }).then((res) => {
        this.userData = res.data
        console.log(this.userData)
      }).catch((err) => {
        console.log(err.data)
      })
    }
  }
}
</script>

<style>
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