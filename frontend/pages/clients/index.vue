<template>
    <b-container class="mt-5">
        <b-card header="Clients">
            <b-table striped hover :items="clients"></b-table>
        </b-card>
    </b-container>
</template>

<script>
    export default {
        name: "clients",
        head: () => ({
            title: 'Clients'
        }),
        data: () => ({
            clients: []
        }),
        mounted() {
            this.$axios.get('/clients')
                .then(({data}) => this.clients = data)
        }
    }
</script>
