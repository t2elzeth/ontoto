<template>
  <div class="main">
    <h1 id="logo">ONTOTO</h1>
    <div class="nav-right-block">
      <router-link to="/about">О НАС</router-link>

      <a href="#">
        <img src="../../assets/images/icons/phone.svg" alt="" class="phone" />
        моб.приложение
      </a>
      <img src="../../assets/images/icons/heart.svg" alt="" class="heart" />
      <hr class="divider" />
      <router-link to="/signup">РЕГИСТРАЦИЯ</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style scoped lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Fjalla+One&display=swap");
.main {
  padding: 0 100px;
  text-align: left;
  color: white;
  height: 90px;

  display: flex;
  align-items: center;
  justify-content: space-between;

  font-family: Fjalla One, sans-serif;
  font-style: normal;
  font-weight: normal;

  background: linear-gradient(
    270.02deg,
    rgba(29, 42, 158, 0.81) 47.21%,
    rgba(29, 42, 158, 0) 149.13%
  );
  box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
  filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25));

  #logo {
    font-size: 72px;
    line-height: 90px;
    letter-spacing: 0.1em;
  }

  a {
    text-decoration: none;
    color: white;
    font-size: 20px;
    display: flex;
    align-items: center;
  }

  .nav-right-block {
    width: 750px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    .phone {
      width: 30px;
      height: 35px;
    }

    .heart {
      width: 45px;
      height: 45px;
    }

    .divider {
      width: 90px;
      height: 0;
      transform: rotate(-90deg);
      color: white;
    }
  }
}
</style>
