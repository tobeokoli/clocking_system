import Vue from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import HomeScreen from "./components/HomeScreen.vue";
import ClockIn from "./components/ClockIn.vue";

Vue.use(VueRouter);
const router = new VueRouter({
  routes: [
    { path: "/", component: HomeScreen }, // Example route
    { path: "/clock-in", component: ClockIn },
  ],
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
