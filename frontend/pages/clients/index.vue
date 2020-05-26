<template>
    <b-container>
        <DataTable
            title="Clients"
            destination="/clients/create"
            :items="clients"
            :fields="['id', 'name', 'firm', 'actions']"
            :delete-item="deleteItem"
        />
    </b-container>
</template>

<script>
import DataTable from '@/components/DataTable'

export default {
    name: 'Clients',
    components: { DataTable },
    data: () => ({
        clients: [],
    }),
    mounted() {
        this.$axios.get('/clients').then(({ data }) => (this.clients = data))
    },
    methods: {
        deleteItem(client) {
            this.$axios
                .delete('/clients', {
                    data: {
                        id: client.id,
                    },
                })
                .then(
                    (_) =>
                        (this.clients = this.clients.filter(
                            (e) => e.id !== client.id
                        ))
                )
        },
    },
    head: () => ({
        title: 'Clients',
    }),
}
</script>
