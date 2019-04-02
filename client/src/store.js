import Vue from 'vue'
import Vuex from 'vuex'
import router from './router'
import { axiosRequests } from 'axios'

Vue.use(Vuex)

export function parseUserFromToken(token) {
    let payload = token.split(".")[1]
    let parsedPayload = JSON.parse(atob(payload))

    let user = {
        username: parsedPayload.sub
    }
    return user
}

const store = new Vuex.Store({
    state: {
        user: null
    },
    getters: {
        isLoggedIn(state) {
            return !!state.user
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
            axiosRequests.defaults.headers.authorization = null
            localStorage.removeItem('token')
            commit('resetState')
        },
        setSystemMessage({ commit }, payload) {
            commit('setSystemMessage', payload)
        },
        loginFromForm({ commit }, payload) {
            //using axios.post directly since login route is different namespace from API
            axiosRequests.post('/login')
                .then(resp => {
                    const token = resp.body.access_token
                    // We need to modify the API axios instance to send the new token with the requests
                    const user = parseUserFromToken(token)
                    axiosRequests.defaults.headers.authorization = token
                    localStorage.setItem("token", token)
                    commit('setUser', { user })
                    router.push("/")
                })
                .catch(err => {
                    if (err.response && err.response.status === 403) {
                        commit(
                            'setSystemMessage',
                            { message: "Unable to verify credentials, please check credentials and try again" }
                        )
                    } else {
                        commit(
                            'setSystemMessage',
                            { message: "Something went wrong, please try again in a few minutes" }
                        )
                    }
                })
        }
    }
})

export default store