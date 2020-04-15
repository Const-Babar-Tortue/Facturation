import apiClient from '@/api'

export default {
    async login({username, password}) {
        try {
            const {data} = await apiClient.post('/auth', {
                username,
                password
            })
            return {token: data["access_token"]}
        } catch (e) {
            if (e.response && e.response.status === 401)
                return Promise.reject({invalid: true})
            else
                return Promise.reject({error: true})
        }

    }
}
