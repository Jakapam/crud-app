import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Login from './pages/Login'
import Admin from './pages/Admin'
import Home from './pages/Home'
import store from './store'

Vue.use(VueRouter)

const router = new VueRouter({
    mode: 'history',
    routes: [
        {
            path: '/', component: App,
            children: [
                { path: "login", component: Login, name: "login" },
                { path: "admin", component: Admin, name: "admin" },
                { path: "", component: Home, name: "home" }
            ]
        }
    ],
    path: '*', redirect: '/'
})

router.beforeResolve((to, from, next) => {
    if(to.path != '/login') {
        if(localStorage.getItem("token")) { 
            next();
        } else {
            next('login');
        }
    } else {
        if(localStorage.getItem("token")) { 
            next('admin');
        } else {
            next();
        }
    }
});

export default router