import { createRouter, createWebHistory } from 'vue-router'
/* import Customers from '../modules/customers/Customers.vue' */
import store from '../store'

const routes = [
  // Vue routes
  {path: '/',name: 'Home',component: () => import('../views/Home.vue')},
  {path: '/about',name: 'About',component: () => import('../views/About.vue')},
   // Sign-in routes
  {path: '/sign-up', name: 'SignUp',component: () => import ('../views/LogIn.vue')},
  {path: '/log-in',name: 'LogIn', component: () => import('../views/LogIn.vue')},
  {path: '/dashboard', name: 'Dashboard',component: () => import('../views/dashboard/Dashboard.vue'),meta: { requireLogin: true} },
  {path: '/dashboard/my-account',name: 'MyAccount', component: () => import('../views/dashboard/MyAccount.vue'), meta: { requireLogin: true}},
  // Customer routes
  {path: '/customers', name: 'Customers', component: () => import ('../modules/customers/Customers.vue'), meta: {requireLogin:true}},
  {path: '/customers/add', name: 'AddCustomer', component: () => import ('../modules/customers/AddCustomer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id', name: 'Customer', component: () => import ('../modules/customers/Customer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id/edit', name: 'CustomerEdit', component: () => import ('../modules/customers/EditCustomer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id/delete', name: 'CustomerDelete', component: () => import ('../modules/customers/DeleteCustomer.vue'), meta: {requireLogin:true}},
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')
  } else {
    next()
  }
})

export default router
