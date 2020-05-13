<template>
    <b-container>
        <DataTable
            title="Bills"
            destination="/bills/create"
            :items="bills"
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
    head: () => ({
        title: 'Bills',
    }),
}
</script>
