export const state = () => ({
    clients: [],
})

export const mutations = {
    set(state, bills) {
        state.clients = bills
    },
    delete(state, id) {
        state.clients = state.clients.filter((e) => e.id !== id)
    },
}

export const actions = {
    load({ commit }) {
        this.$axios.get('/clients').then(({ data }) => commit('set', data))
    },
    delete({ commit }, { id }) {
        this.$axios.delete(`/clients/${id}`).then((_) => commit('delete', id))
    },
}

export const getters = {}
