<template>
  <div class="footer">
    <div class="container">
      <div class="links-container">
        <div class="links">
          <a href="#">Конфиденциальность</a>
          <a href="#">Платные услуги</a>
          <a href="#">Бизнес профиль</a>
          <a href="#">Правила безопасности</a>
        </div>
        <div class="links">
          <a href="#">Реклама на сайте</a>
          <a href="#">Связаться с нами</a>
          <a href="#">О нас</a>
        </div>
      </div>
      <div class="mobile-app-container">
        <p>Скачать наше приложение</p>
        <div class="mobile-stores">
          <img src="../../assets/images/icons/appstore.svg" alt="App store" />
          <img
            src="../../assets/images/icons/google-play.svg"
            alt="Google play"
          />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Footer"
};
</script>

<style scoped lang="scss">
@import "../../assets/vars";

.footer {
  width: 100%;
  height: 310px;

  display: flex;
  align-items: center;

  background: $white;
  color: $black;

  font-family: Comfortaa, cursive;
  font-style: normal;
  font-weight: normal;
  font-size: 20px;
  line-height: 22px;
  letter-spacing: 0.1em;
  text-align: left;

  .container {
    height: 170px;

    margin-left: 100px;

    display: flex;

    .links-container {
      width: 670px;

      display: flex;
      justify-content: space-between;
      align-items: start;

      a {
        display: block;
        height: 42px;
        text-decoration: none;
        color: inherit;
      }
    }

    .mobile-app-container {
      margin-left: 205px;

      p {
        display: block;

        font-size: 20px;
      }

      .mobile-stores {
        display: inline-block;
        margin-left: -10px;

        img {
          width: 245px;
          height: 90px;
        }
      }
    }
  }
}
</style>
