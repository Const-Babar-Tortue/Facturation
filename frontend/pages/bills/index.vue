<template>
    <b-container>
        <DataTable title="Bills" destination="/bills/create" :items="bills">
            <template v-slot>
                <b-modal id="info-modal" hide-footer>
                    <div class="d-block text-center">
                        <h3>Info</h3>
                        <h2>{{ info.subject }}</h2>
                    </div>
                    <b-list-group>
                        <b-list-group-item>ID: {{ info.id }}</b-list-group-item>
                        <b-list-group-item>
                            Cash: {{ info.cash }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Date: {{ info.date }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Date: {{ info.expiration }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Date: {{ info.paid }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Date: {{ info.price }}
                        </b-list-group-item>
                    </b-list-group>
                    <div class="d-block text-center">
                        <h2>Client</h2>
                    </div>
                    <b-list-group>
                        <b-list-group-item>
                            ID: {{ client.id }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Name: {{ client.name }}
                        </b-list-group-item>
                        <b-list-group-item>
                            City: {{ client.postalCode }}, {{ client.city }}
                        </b-list-group-item>
                        <b-list-group-item>
                            Address: {{ client.city }},
                            {{ client.streetNumber }}
                        </b-list-group-item>
                        <b-list-group-item>
                            VAT number: {{ client.vatNumber }}
                        </b-list-group-item>
                    </b-list-group>
                </b-modal>

                <b-table
                    class="m-0"
                    responsive=""
                    striped
                    hover
                    :items="bills"
                    :fields="fields"
                >
                    <template v-slot:cell(paid)="row">
                        <b-badge v-if="row.item.paid" variant="success">
                            Yes
                        </b-badge>
                        <b-badge v-else variant="danger">No</b-badge>
                    </template>
                    <template v-slot:cell(actions)="row">
                        <b-button size="sm" @click="toggle(row.item)">
                            Toggle
                        </b-button>
                        <b-button size="sm" @click="showInfo(row.item)">
                            More info
                        </b-button>
                        <b-button size="sm" @click="deleteBill(row.item)">
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
    name: 'Bills',
    components: { DataTable },
    data: () => ({
        selectedItem: null,
        info: '',
        client: '',
        fields: [
            { key: 'id', sortable: true },
            { key: 'subject', sortable: true },
            { key: 'price', sortable: true },
            { key: 'paid', sortable: true },
            { key: 'date', sortable: true },
            { key: 'expiration', sortable: true },
            { key: 'actions', sortable: false },
        ],
    }),
    computed: {
        ...mapState('bills', { bills: (state) => state.bills }),
    },
    mounted() {
        this.$store.dispatch('bills/load')
    },
    methods: {
        ...mapActions({ deleteBill: 'bills/delete', toggle: 'bills/toggle' }),
        showInfo(item) {
            this.info = item
            this.$axios
                .get(`/clients/${item.clientId}`)
                .then(({ data }) => (this.client = data))
            this.$bvModal.show('info-modal')
        },
    },
    head: () => ({
        title: 'Bills',
    }),
}
</script>
