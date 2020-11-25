<template>
  <div class="app">
    <form action="" class="form" @submit.prevent="submitForm">
      <div class="form-field">
        <label for="id_email">Почта</label>
        <input type="text" id="id_email" v-model="formData.email" />
      </div>

      <div class="form-field">
        <label for="id_password">Пароль</label>
        <input type="password" id="id_password" v-model="formData.password" />
      </div>

      <input type="submit" value="Sign up" />
    </form>
  </div>
</template>

<script>
export default {
  name: "Login",
  setup() {
    const msg = "Salamaleksus ebana";
    const formData = {
      email: "",
      password: ""
    };

    function submitForm() {
      console.log(formData);
    }

    return {
      msg,
      formData,
      submitForm
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
