import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import { axiosRequest } from './main'

Vue.use(Vuex)

export function parseUserFromToken(token) {
    let payload = token.split(".")[1]
    let parsedPayload = JSON.parse(atob(payload))

    let user = {
        username: parsedPayload.identity
    }
    return user
}

const store = new Vuex.Store({
    state: {
        user: null
    },
    getters: {
        isLoggedIn(state){
            let token = localStorage.getItem("token")
            let loggedIn = !!state.user || token
            return loggedIn
        }
    },
    mutations: {
        setUser(state, payload) {
            state.user = payload.user
        },
        resetState(state, payload) {
            state.user = null
        }
    },
    actions: {
        logout({ commit }, payload) {
            axiosRequest.defaults.headers.authorization = null
            localStorage.removeItem('token')
            commit('resetState')
        },
        loginFromForm({ commit }, payload) {
            axiosRequest.post('/login',{
                username: payload.username,
                password: payload.password
              }).then(({data}) => {
                    const token = data.access_token
                    axiosRequest.defaults.headers.authorization = token
                    const user = parseUserFromToken(token)
                    localStorage.setItem("token", token)
                    commit('setUser', { user })
                    router.push("/admin")
                }).catch(err => {
                    console.log(err)
                })
        }
    }
})

export default store