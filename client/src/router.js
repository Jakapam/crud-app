import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Login from './components/Login'
import Admin from './components/Admin'
import Home from './components/Home'

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

export default router