<template>
  <div class="choose-action">
    <router-link
      tag="a"
      class="action"
      :class="{ active: focusOn === 'login' }"
      to="/login"
    >
      ВХОД
      <hr />
    </router-link>
    <router-link
      to="/signup"
      class="action"
      :class="{ active: focusOn === 'signup' }"
    >
      РЕГИСТРАЦИЯ
      <hr />
    </router-link>
  </div>
  <div class="social-auth">
    <div class="links">
      <a href="#">
        <img src="../../assets/images/icons/facebook.svg" alt="Facebook" />
      </a>
      <a href="#">
        <img src="../../assets/images/icons/google-auth.svg" alt="Google" />
      </a>
      <a href="#">
        <img src="../../assets/images/icons/vk.svg" alt="VK" />
      </a>
    </div>
    <div class="or">
      <hr />
      или
      <hr />
    </div>
  </div>
</template>

<script>
export default {
  name: "FormHeader",
  props: {
    focusOn: {
      type: String,
      required: true
    }
  }
};
</script>

<style scoped lang="scss">
@import "../../assets/vars";
$focus-color: #3c47a5;

.choose-action {
  width: 100%;
  height: 90px;

  display: flex;
  justify-content: space-between;
  align-items: center;

  .action {
    font-weight: bold;
    font-size: 24px;
    color: white;

    display: flex;
    flex-direction: column;
    justify-content: space-around;

    text-transform: uppercase;
    text-align: center;
    text-decoration: none;
    width: 50%;
    height: 100%;

    hr {
      width: 100%;
      border: 3px solid white;
    }
  }
  .active {
    color: $focus-color;

    hr {
      border-color: $focus-color;
    }
  }
}

.social-auth {
  height: 145px;

  display: flex;
  flex-direction: column;
  justify-content: space-around;

  .links {
    padding: 0 50px;

    display: flex;
    justify-content: space-around;
    align-items: center;

    img {
      width: 80px;
      height: 80px;
    }
  }

  .or {
    display: flex;
    justify-content: space-between;
    align-items: center;

    hr {
      border-color: $hr-color;

      width: 45%;
      height: 1px;
    }
  }
}
</style>
