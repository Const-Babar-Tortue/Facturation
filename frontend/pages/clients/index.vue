<template>
    <b-container>
        <DataTable
            title="Clients"
            destination="/clients/create"
            :items="clients"
        >
            <template v-slot>
                <b-table
                    class="m-0"
                    responsive=""
                    striped
                    hover
                    :items="clients"
                    :fields="fields"
                >
                    <template v-slot:cell(paid)="row">
                        <b-badge v-if="row.item.paid" variant="success">
                            Yes
                        </b-badge>
                        <b-badge v-else variant="danger">No</b-badge>
                    </template>
                    <template v-slot:cell(actions)="row">
                        <b-button size="sm" @click="deleteClient(row.item)">
                            Delete
                        </b-button>
                    </template>
                </b-table>
            </template>
        </DataTable>
    </b-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import DataTable from '@/components/DataTable'

export default {
    name: 'Clients',
    components: { DataTable },
    data: () => ({
        selectedItem: null,
        fields: ['id', 'name', 'firm', 'actions'],
    }),
    computed: {
        ...mapState('clients', { clients: (state) => state.clients }),
    },
    mounted() {
        this.$store.dispatch('clients/load')
    },
    methods: {
        ...mapActions({ deleteClient: 'clients/delete' }),
    },
    head: () => ({
        title: 'Clients',
    }),
}
</script>
