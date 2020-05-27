export const state = () => ({
    bills: [],
})

export const mutations = {
    set(state, bills) {
        state.bills = bills
    },
    delete(state, id) {
        state.bills = state.bills.filter((e) => e.id !== id)
    },
    toggle(state, id) {
        state.bills = state.bills.map((e) =>
            e.id === id ? { ...e, paid: !e.paid } : e
        )
    },
}

export const actions = {
    load({ commit }) {
        this.$axios.get('/bills').then(({ data }) => commit('set', data))
    },
    delete({ commit }, { id }) {
        this.$axios.delete(`/bills/${id}`).then((_) => commit('delete', id))
    },
    toggle({ commit }, { id }) {
        commit('toggle', id)
    },
}

export const getters = {}
