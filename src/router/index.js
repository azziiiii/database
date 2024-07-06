import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path:'/',
        name:'home',
        component: ()=>import('../pages/Home.vue'),
        redirect: '/home',
        children:[
            {path: 'home', name: "home", component:()=>import('../pages/welcome.vue')},
            {path: 'athlete', name: "athlete", component:()=>import('../pages/athlete.vue')},
            {path: 'tmplate', name: "tmplate", component:()=>import('../pages/tmplate.vue')},
            {path: '1', name:'1', component:()=>import("../pages/athlete/1.vue")},
            {path: '2', name:'2', component:()=>import("../pages/athlete/2.vue")},
            {path: '3', name:'3', component:()=>import("../pages/athlete/3.vue")},
            {path: '4', name:'4', component:()=>import("../pages/teacher/1.vue")},
            {path: '5', name:'5', component:()=>import("../pages/teacher/2.vue")},
            {path: '6', name:'6', component:()=>import("../pages/teacher/3.vue")},
            {path: '7', name:'7', component:()=>import("../pages/admin/1.vue")},
            {path: '8', name:'8', component:()=>import("../pages/admin/2.vue")},
            // {path: '9', name:'9', component:()=>import("../pages/admin/3.vue")},
        ]
    },
    {
        path:'/login',
        name:'Login',
        component: ()=>import('../pages/Login.vue')
    },
    {
        path:'/403',
        name:'Auth',
        component: ()=>import('../pages/auth.vue')
    },
    {
        path:'/register',
        name:'Register',
        component: ()=>import('../pages/Register.vue')
    },
    {
        path:'/404',
        name:'404',
        component: ()=>import('../pages/404.vue')
    }
]

const router = new VueRouter({
    mode:'history',
    base: process.env.BASE_URL,
    routes
})

// const roleRoutes = {
//     学生: ['/student'],
//     教师: ['/teacher'],
//     管理员: ['/home']
// };

// router.beforeEach((to, from, next) => {

//     let user = JSON.parse(localStorage.getItem('User') || '{}')
//     let userRole = user.role;
//     if(!roleRoutes[userRole].includes(to.path))
//     {
//         next('/403')
//     }
//     else
//     {
//         next()
//     }
// })

export default router