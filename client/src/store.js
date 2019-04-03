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
        user: null,
        tokens: [],
        questions: []
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
        },
        setResources(state, payload){
            state[payload.resource] = payload.objects
        }
    },
    actions: {
        getManyResources({ commit },{ resource }){
            const resourceCapitalize = resource.charAt(0).toUpperCase() + resource.slice(1)
            axiosRequest.get(`${resource}`).then(({data})=>{
                let payload = { 
                    resource: `${resource}s`,
                    objects: data.objects  
                }
                commit('setResources', payload)
            })
        },
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
                    router.push("/admin")
                    localStorage.setItem("token", token)
                    commit('setUser', { user })
                }).catch(err => {
                    console.log(err)
                })
        }
    }
})

export default store