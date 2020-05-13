<template>
    <b-container class="mt-5">
        <DataTable
            title="Clients"
            destination="/clients/create"
            :items="clients"
        ></DataTable>
    </b-container>
</template>

<script>
    import DataTable from "@/components/DataTable";

    export default {
        name: "clients",
        components: {DataTable},
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
