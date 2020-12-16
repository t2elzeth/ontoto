<template>
  <div class="choose-action">
    <a href="#" class="action" :ref="refs.login">
      ВХОД
      <hr />
    </a>
    <a href="#" class="action" :ref="refs.signup">
      РЕГИСТРАЦИЯ
      <hr />
    </a>
  </div>
  <div class="social-auth"></div>
</template>

<script>
import { ref, onMounted } from "vue";

export default {
  name: "FormHeader",
  props: {
    focusOn: {
      type: String
    }
  },
  setup() {
    const refs = {
      login: ref(),
      signup: ref()
    };

    onMounted(() => {
      console.log(refs.login.value.focus());
    });

    return {
      refs
    };
  }
};
</script>

<style scoped lang="scss">
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

    &:focus {
      color: $focus-color;

      hr {
        border-color: $focus-color;
      }
    }

    hr {
      width: 100%;
      border: 3px solid white;
    }
  }
}

.social-auth {
  height: 145px;
}
</style>
