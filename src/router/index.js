import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/cart',
    name: 'Cart',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Cart')
  },
  {
    path:'/list',
    name:'List',
    component: ()=>import('../views/List')
  },
  {
    path:'/login',
    name:'Login',
    component: ()=>import('../views/Login')
  },
  {
    path:'/detail',
    name:'Detail',
    component: ()=>import('../views/Detail')
  },
  {
    path:'/register',
    name:'Register',
    component: ()=>import('../views/Register')
  },
  {
    path:'/user_center_info',
    name:'UserCenterInfo',
    component: ()=>import('../views/UserCenterInfo')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
