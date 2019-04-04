import Vue from 'vue'
import Vuex from 'vuex'
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
            debugger
            axiosRequest.get(`${resource}`).then(({data})=>{
                let payload = { 
                    resource: `${resource}s`,
                    objects: data.objects  
                }
                commit('setResources', payload)
            })
        },
        logout({ commit }, payload) {
            axiosRequest.defaults.headers.Authorization = null
            localStorage.removeItem('token')
            commit('resetState')
        },
        loginFromForm({ commit }, payload) {
            return axiosRequest.post('/login',{
                username: payload.username,
                password: payload.password
              }).catch(err => {
                console.log(err)
            })
        }
    }
})

export default store