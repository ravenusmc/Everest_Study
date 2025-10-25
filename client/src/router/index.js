import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import store from '@/store/index';

Vue.use(VueRouter)

const routes = [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/about',
      name: 'AboutView',
      component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
      path: '/data',
      name: 'DataView',
      component: () => import('../views/DataView.vue'),
      beforeEnter: (to, from, next) => {
        if (store.state.user.loginFlag === false) {
          next('/login');
        } else {
          next();
        }
    },
    beforeRouteLeave: (to, from, next) => {
      if (store.state.user.loginFlag === false) {
        next('/login');
      } else {
        next();
      }
    },
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: () => import('../views/LoginPage.vue')
    },    
    {
      path: '/signup',
      name: 'SignUpPage',
      component: () => import('../views/SignUpPage.vue')
    },
  ]
  
  const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })
  
  export default router