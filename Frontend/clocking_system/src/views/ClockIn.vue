<template>
  <div class="screen">
    <div class="left">
      <p></p>
    </div>
    <div class="right">
      <h1 id="clock">Clock In</h1>
      <p id="subtitle">Enter your correct details and submit to clock in</p>
      <div id="labeled-input">
        <p>Username</p>
        <input class="input top-input" type="text" v-model="form.username" />
      </div>
      <div id="labeled-input">
        <p>Password</p>
        <input class="input" type="password" v-model="form.password" />
      </div>
      <button id="button" @click="clockIn">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "ClockIn",
  methods: {
    async clockIn() {
      try {
        // Replace 'your-api-endpoint' with your actual clock-in endpoint URL
        const response = await axios.post(
          "http://127.0.0.1:8000/api/clock-in/",
          { username: this.form.username, password: this.form.password }
        );
        console.log(response.data);
        // Check if the response status is successful (e.g., status code 200)
        if (response.status === 200 || response.status === 201) {
          // Show a success prompt (you can use a notification library or custom message)
          alert(response.data.message);

          // Redirect to the home page or another route if needed
          this.$router.push("/");
        } else {
          // Handle other response statuses or errors
          alert(response.data.message);
        }
      } catch (error) {
        // Handle Axios request error
        console.error("Error:", error);

        // Show an error prompt (you can use a notification library or custom message)
        alert(error.response.data.message);

        // Redirect to the home page or another route if needed
        this.$router.push("/");
      }
    },
  },
  // Your component options here
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
    };
  },
};
</script>

<style>
/* Your component styles here */
.left {
  background-color: rgba(20, 110, 24, 0.3);
}
#button {
  margin-top: 40px;
  background-color: green;
  margin-right: 10px;
  /* margin-top: 50px; */
  color: white;
  border: none; /* Remove the border */
  border-radius: 10px; /* Add rounded corners */
  padding: 25px 30px; /* Add padding for spacing */
  cursor: pointer;
  width: 200px;
}
#clock {
  /* padding-bottom: 30px; */
}
.top_input {
  margin-bottom: 30px;
}
#subtitle {
  padding-bottom: 60px;
}
.input {
  border-radius: 10px;
  width: 250px;
  height: 46px;
  background: #d9d9d9;
}
.right {
  /* background-color: rgba(20, 110, 24, 0.3); */
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.screen {
  display: grid;
  grid-template-columns: 1fr 1fr;
}
</style>
