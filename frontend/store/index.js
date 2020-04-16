import {clearToken, setToken} from "@/services/LocalStorageService";

export const state = () => ({
    token: ''
})

export const mutations = {
    setToken(state, token) {
        state.token = token
        setToken(token)
    },
    clearToken(state) {
        state.token = null
        clearToken()
    },
    initToken(state) {
        state.token = localStorage.getItem('token')
    }
}

export const actions = {}

export const getters = {
    isLoggedIn(state) {
        return state.token !== null && state.token !== ''
    }
}
