import axios from 'axios'

import {mapState} from "vuex";

const state = mapState(['token'])

const apiClient = axios.create({
    baseURL: `http://localhost:5000`,
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
