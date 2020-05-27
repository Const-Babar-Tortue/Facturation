<template>
    <b-container>
        <DataTable
            title="Bills"
            destination="/bills/create"
            :items="bills"
            :fields="[
                'id',
                'subject',
                'price',
                'paid',
                'date',
                'expiration',
                'actions',
            ]"
            :delete-item="deleteBill"
        ></DataTable>
    </b-container>
</template>

<script>
import { mapState, mapActions } from 'vuex'
import DataTable from '@/components/DataTable'

export default {
    name: 'Index',
    components: { DataTable },
    computed: {
        ...mapState('bills', { bills: (state) => state.bills }),
    },
    mounted() {
        this.$store.dispatch('bills/load')
    },
    methods: mapActions({ deleteBill: 'bills/delete' }),
    head: () => ({
        title: 'Bills',
    }),
}
</script>
