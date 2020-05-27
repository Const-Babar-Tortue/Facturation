<template>
    <b-container>
        <DataTable title="Bills" destination="/bills/create" :items="bills">
            <template v-slot>
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
        fields: [
            'id',
            'subject',
            'price',
            'paid',
            'date',
            'expiration',
            'actions',
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
    },
    head: () => ({
        title: 'Bills',
    }),
}
</script>
