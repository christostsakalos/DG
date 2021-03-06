import { createRouter, createWebHistory } from 'vue-router'
/* import Customers from '../modules/customers/Customers.vue' */
import store from '../store'

const routes = [
  // Vue routes
   {path: '/',name: 'LogIn', component: () => import('../views/LogIn.vue')},
  /*{path: '/about',name: 'About',component: () => import('../views/About.vue')}, */
   // Sign-in routes
  {path: '/log-in',name: 'LogIn', component: () => import('../views/LogIn.vue')},
  //{path: '/sign-up', name: 'SignUp',component: () => import ('../views/LogIn.vue')},
  {path: '/dashboard', name: 'Dashboard',component: () => import('../views/dashboard/Dashboard.vue'),meta: { requireLogin: true} },
  {path: '/dashboard/my-account',name: 'MyAccount', component: () => import('../views/dashboard/MyAccount.vue'), meta: { requireLogin: true}},
  // Customer routes
  {path: '/customers', name: 'Customers', component: () => import ('../modules/customers/Customers.vue'), meta: {requireLogin:true}},
  {path: '/customers/add', name: 'AddCustomer', component: () => import ('../modules/customers/AddCustomer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id', name: 'Customer', component: () => import ('../modules/customers/Customer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id/edit', name: 'CustomerEdit', component: () => import ('../modules/customers/EditCustomer.vue'), meta: {requireLogin:true}},
  {path: '/customers/:id/delete', name: 'CustomerDelete', component: () => import ('../modules/customers/DeleteCustomer.vue'), meta: {requireLogin:true}},
  
  // Vehicle routes
  {path: '/vehicles', name: 'Vehicles', component: () => import ('../modules/vehicles/Vehicles.vue'), meta: {requireLogin:true}},
  {path: '/vehicles/add', name: 'AddVehicle', component: () => import ('../modules/vehicles/AddVehicle.vue'), meta: {requireLogin:true}},
  {path: '/vehicles/:id', name: 'Vehicle', component: () => import ('../modules/vehicles/Vehicle.vue'), meta: {requireLogin:true}},
  {path: '/vehicles/:id/edit', name: 'VehicleEdit', component: () => import ('../modules/vehicles/EditVehicle.vue'), meta: {requireLogin:true}},
  {path: '/vehicles/:id/delete', name: 'VehicleDelete', component: () => import ('../modules/vehicles/DeleteVehicle.vue'), meta: {requireLogin:true}},

  // Inventory - Categories
  {path: '/categories', name: 'Categories', component: () => import ('../modules/inventory/categories/Categories.vue'), meta: {requireLogin:true}},
  {path: '/categories/add', name: 'AddCategory', component: () => import ('../modules/inventory/categories/components/AddCategory.vue'), meta: {requireLogin:true}},
  {path: '/categories/:id', name: 'Category', component: () => import ('../modules/inventory/categories/components/Category.vue'), meta: {requireLogin:true}},
  {path: '/categories/:id/edit', name: 'CategoryEdit', component: () => import ('../modules/inventory/categories/components/EditCategory.vue'), meta: {requireLogin:true}},
  {path: '/categories/:id/delete', name: 'CategoryDelete', component: () => import ('../modules/inventory/categories/components/DeleteCategory.vue'), meta: {requireLogin:true}},
  {path: '/subcategories/add', name: 'AddSubcategory', component: () => import ('../modules/inventory/categories/components/AddSubcategory.vue'), meta: {requireLogin:true}},
  {path: '/subcategories/:id', name: 'Subcategory', component: () => import ('../modules/inventory/categories/components/Subcategory.vue'), meta: {requireLogin:true}},
  {path: '/subcategories/:id/edit', name: 'SubcategoryEdit', component: () => import ('../modules/inventory/categories/components/EditSubcategory.vue'), meta: {requireLogin:true}},
  {path: '/subcategories/:id/delete', name: 'SubcategoryDelete', component: () => import ('../modules/inventory/categories/components/DeleteSubcategory.vue'), meta: {requireLogin:true}},
  // Inventory - Categories
  {path: '/parts', name: 'Parts', component: () => import ('../modules/inventory/inventoryparts/Parts.vue'), meta: {requireLogin:true}},
  {path: '/parts/add', name: 'AddPart', component: () => import ('../modules/inventory/inventoryparts/AddPart.vue'), meta: {requireLogin:true}},
  {path: '/parts/:id', name: 'Part', component: () => import ('../modules/inventory/inventoryparts/Part.vue'), meta: {requireLogin:true}},
  {path: '/parts/:id/edit', name: 'PartEdit', component: () => import ('../modules/inventory/inventoryparts/EditPart.vue'), meta: {requireLogin:true}},
  {path: '/parts/:id/delete', name: 'PartDelete', component: () => import ('../modules/inventory/inventoryparts/DeletePart.vue'), meta: {requireLogin:true}},
  // Invoice
  {path: '/invoices/add', name: 'AddInvoice', component: () => import ('../modules/invoices/AddInvoice.vue'), meta: {requireLogin:true}},
  {path: '/invoices', name: 'Invoices', component: () => import ('../modules/invoices/Invoices.vue'), meta: {requireLogin:true}},
  {path: '/invoices/:id', name: 'Invoice', component: () => import ('../modules/invoices/Invoice.vue'), meta: {requireLogin:true}},
  //To delete invoice if any mistakes occur
  {path: '/invoicesdelete', name: 'Invoicesdelete', component: () => import ('../modules/invoices/InvoicesDel.vue'), meta: {requireLogin:true}},
  // Jobsheets routes
  {path: '/jobsheets', name: 'Jobsheets', component: () => import ('../modules/jobsheets/Jobsheets.vue'), meta: {requireLogin:true}},
  {path: '/jobsheets/add', name: 'AddJobsheet', component: () => import ('../modules/jobsheets/AddJobsheet.vue'), meta: {requireLogin:true}},
  {path: '/jobsheets/:id', name: 'Jobsheet', component: () => import ('../modules/jobsheets/Jobsheet.vue'), meta: {requireLogin:true}},
  {path: '/jobsheets/:id/edit', name: 'JobsheetEdit', component: () => import ('../modules/jobsheets/EditJobsheet.vue'), meta: {requireLogin:true}},
  {path: '/jobsheets/:id/delete', name: 'JobsheetDelete', component: () => import ('../modules/jobsheets/DeleteJobsheet.vue'), meta: {requireLogin:true}},

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
