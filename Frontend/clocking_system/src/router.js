import { createRouter, createWebHistory } from "vue-router";
import ClockIn from "./views/ClockIn.vue";
import ClockOut from "./views/ClockOut.vue";
import HomeScreen from "./views/HomeScreen.vue";

export const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      // You could also have named views at tho top
      component: HomeScreen,
      //   children: [],
    },
    {
      path: "/clock-in",
      // You could also have named views at tho top
      component: ClockIn,
      //   children: [],
    },
    {
      path: "/clock-out",
      // You could also have named views at tho top
      component: ClockOut,
      //   children: [],
    },
  ],
});
