import axios from 'axios'

const apiClient = axios.create({
    baseURL: `http://localhost:5000`,
    withCredentials: false,
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
})

export default {
    async register({username, email, password}) {
        try {
            await apiClient.post('/register', {
                username,
                email,
                password
            })
            return {success: true}
        } catch (e) {
            if (e.response && e.response.status === 409)
                return Promise.reject({exists: true})
            else
                return Promise.reject({error: true})
        }

    }
}