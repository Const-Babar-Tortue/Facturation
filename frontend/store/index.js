import {getToken, clearToken, setToken} from "@/services/LocalStorageService";

export const state = () => ({
    token: getToken()
})

export const mutations = {
    setToken(state, token) {
        state.token = token
        setToken(token)
    },
    clearToken(state){
        state.token = null
        clearToken()
    }
}

export const getters = {}
