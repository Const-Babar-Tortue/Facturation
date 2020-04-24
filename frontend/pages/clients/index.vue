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
        data: () => ({
            clients: []
        }),
        mounted() {
            /*ClientService.clients()
                .then(clients => this.clients = clients)*/
        }
    }
</script>
