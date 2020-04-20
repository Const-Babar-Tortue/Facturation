import axios from 'axios'

import {mapState} from "vuex";

const state = mapState(['token'])

let apiHost = process.env.API_HOST

const apiClient = axios.create({
    baseURL: apiHost,
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
})


axios.interceptors.request.use(
    config => {
        const token = state.token;
        if (token) {
            config.headers['Authorization'] = 'Bearer ' + token;
        }
        return config;
    },
    error => {
        Promise.reject(error)
    });

export default apiClient
