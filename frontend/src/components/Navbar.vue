<template>
  <div class="topnav">
    <div class="navlist">
      <a class="active" href="#">Home</a>
      <a href="#">News</a>
      <a href="#">Contact</a>
      <a href="#">About</a>
    </div>
    <div class="auth">
      <router-link to="/login">Login</router-link> |
      <router-link to="/signup">SignUp</router-link> |
    </div>
  </div>
</template>

<script>
export default {
  name: "Navbar"
};
</script>

<style scoped>
.topnav {
  background-color: #333;
  overflow: hidden;
  margin-left: 160px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 50px;

  position: sticky;
  top: 0;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #4caf50;
  color: white;
}
</style>
