import apiClient from '@/api'

export default {
    async clientNames() {
        try {
            return await apiClient.get('/clients/names')
        } catch (e) {
            return Promise.reject({error: true})
        }
    },

    async clients() {
        try {
            const {data} = await apiClient.get('/clients')
            return data
        } catch (e) {
            return Promise.reject({error: true})
        }
    },
    // pass explicit arguments
    async createClient({name, street, streetNumber, postalCode, city, firm, vatNumber}) {
        try {
            await apiClient.post('/clients', {
                name, street, streetNumber, postalCode, city, firm, vatNumber
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
