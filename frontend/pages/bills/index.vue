<template>
    <b-container class="mt-5">
        <DataTable
            title="Bills"
            destination="/bills/create"
            :items="bills"
        ></DataTable>
    </b-container>
</template>

<script>
    import DataTable from "@/components/DataTable";

    export default {
        name: "index",
        components: {DataTable},
        head: () => ({
            title: 'Bills'
        }),
        data: () => ({
            bills: []
        })
    }
</script>
