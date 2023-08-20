<template>
  <div id="screen">
    <div id="top">
      <img alt="Vue logo" src="../assets/logo.png" />
      <h2>University Of Nigeira, Nsukka</h2>
      <h1 id="vc-office-title">VC Office Clocking System</h1>
    </div>
    <div id="bottom">
      <h2 id="welcome">Welcome</h2>

      <div class="button-wrapper">
        <button id="clock-button" @click="navigateToClockIn">Clock in</button>
        <button id="clock-button">Clock out</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeScreen",
  props: {},
  methods: {
    navigateToClockIn() {
      this.$router.push("/about");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.button-wrapper {
  display: inline-block; /* Ensures container only takes the width of its contents */
}
#top {
  background: rgba(20, 110, 24, 0.3);
}
#vc-office-title {
  /* color: red; */
  padding-bottom: 50px;
}
#welcome {
  padding-top: 30px;
  padding-bottom: 90px;
}
#space20 {
  width: 20px;
}
#clock-button {
  background-color: green;
  margin-right: 10px;
  /* margin-top: 50px; */
  color: white;
  border: none; /* Remove the border */
  border-radius: 10px; /* Add rounded corners */
  padding: 25px 30px; /* Add padding for spacing */
  cursor: pointer;
  width: 250px;
}
</style>
