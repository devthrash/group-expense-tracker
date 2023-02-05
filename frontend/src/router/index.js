import { createRouter, createWebHistory } from 'vue-router'

import TheLogin from "../views/TheLogin.vue";
import MyGroups from "../views/MyGroups.vue";
import TheGroup from "../views/TheGroup.vue";
import NewGroup from "../views/NewGroup.vue";
import TheLogOut from "../views/TheLogOut.vue";

const router = createRouter({
  linkActiveClass: 'is-active',
  linkExactActiveClass: 'is-active',
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/login',
      component: TheLogin
    },
    {
      path: '/logout',
      component: TheLogOut
    },
    {
      path: '/group/:id',
      name: 'view-group',
      component: TheGroup
    },
    {
      path: '/new-group',
      component: NewGroup
    },
    {
      path: '/',
      component: MyGroups
    }
  ]
})

export default router
