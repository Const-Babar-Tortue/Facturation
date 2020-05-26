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
            :delete-item="deleteItem"
        ></DataTable>
    </b-container>
</template>

<script>
import DataTable from '@/components/DataTable'

export default {
    name: 'Index',
    components: { DataTable },
    data: () => ({
        bills: [],
    }),
    mounted() {
        this.$axios.get('/bills').then(({ data }) => (this.bills = data))
    },
    methods: {
        deleteItem(bill) {
            this.$axios
                .delete('/bills', {
                    data: {
                        id: bill.id,
                    },
                })
                .then(
                    (_) =>
                        (this.bills = this.bills.filter(
                            (e) => e.id !== bill.id
                        ))
                )
        },
    },
    head: () => ({
        title: 'Bills',
    }),
}
</script>
