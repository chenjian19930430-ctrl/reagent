import { createRouter, createWebHistory } from "vue-router"
const routes = [
  {path:"/login",component:()=>import("../views/Login.vue")},
  {path:"/",component:()=>import("../layouts/Dashboard.vue"),children:[
    {path:"",redirect:"/dashboard"},
    {path:"dashboard",component:()=>import("../views/Dashboard/index.vue")},
    {path:"videos",component:()=>import("../views/Videos/index.vue")},
    {path:"cs",component:()=>import("../views/CustomerService/index.vue")},
    {path:"leads",component:()=>import("../views/Leads/index.vue")},
    {path:"marketing",component:()=>import("../views/Marketing/index.vue")},
    {path:"documents",component:()=>import("../views/Documents/index.vue")},
  ]},
]
export default createRouter({history:createWebHistory(),routes})
