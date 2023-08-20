<template>
  <div id="screen">
    <div id="top">
      <img id="unn-logo" alt="Vue logo" src="../assets/UNN_logo.gif" />
      <br />
      <h2>University Of Nigeira, Nsukka</h2>
      <h1 id="vc-office-title">VC Office Clocking System</h1>
    </div>
    <div id="bottom">
      <h2 id="welcome">Welcome</h2>

      <div class="button-wrapper">
        <button id="clock-button" @click="navigateToClockIn">Clock in</button>
        <button id="clock-button" @click="navigateToClockOut">Clock out</button>
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
      this.$router.push("/clock-in");
    },
    navigateToClockOut() {
      this.$router.push("/clock-out");
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

.button-wrapper {
  display: inline-block; /* Ensures container only takes the width of its contents */
}
#unn-logo {
  height: 150px;
}
#top {
  background: rgba(20, 110, 24, 0.3);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 50vh;
}
#bottom {
  display: flex;
  flex-direction: column;
  align-items: center;
}
/* #vc-office-title {
  /* color: red; */
/* padding-bottom: 50px; */
/* } */
#welcome {
  padding-top: 30px;
  padding-bottom: 70px;
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
