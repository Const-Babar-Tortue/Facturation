<template>
    <b-container>
        <DataTable
            title="Bills"
            destination="/bills/create"
            :items="bills"
            :fields="['id', 'subject', 'price', 'paid', 'date', 'expiration']"
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
    head: () => ({
        title: 'Bills',
    }),
}
</script>
