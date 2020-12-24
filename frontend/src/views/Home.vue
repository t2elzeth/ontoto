<template>
  <div class="home">
    <form action="#">
      <div class="search">
        <input type="text" placeholder="поиск товаров" />
        <button class="search-btn">
          <img src="../assets/images/icons/search.svg" alt="Search" />
        </button>
        <div class="category">
          <button class="choose-category-btn">выберите категорию</button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>

<style scoped lang="scss">
.home {
  display: flex;
  flex-direction: column;
  align-items: center;

  form {
    margin: 110px 0;
    .search {
      width: 1385px;
      height: 80px;
      border: 1px solid rgba(0, 0, 0, 0.35);
      border-radius: 25px;

      display: flex;
      justify-content: space-between;

      input {
        width: 60%;
        border: none;

        margin-left: 80px;

        &::placeholder {
          //font-family: Rockwell, Comfortaa, cursive;
          //font-style: normal;
          //font-weight: normal;
          font-size: 35px;
          letter-spacing: 0.055em;

          color: rgba(0, 0, 0, 0.6);
        }
      }

      .search-btn {
        width: 10%;

        margin-right: -10px;
        z-index: 3;

        background: rgba(7, 17, 69, 0.77);
        border: none;
        border-radius: 40px;
      }

      .category {
        width: 30%;
        background: #e5e7f1;
        border-top-right-radius: 25px;
        border-bottom-right-radius: 25px;

        display: flex;
        justify-content: center;
        align-items: center;

        .choose-category-btn {
          border: none;
          background: none;

          font-size: 24px;
        }
      }
    }
  }
}
</style>
