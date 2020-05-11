<template>
    <b-container class="mt-5">
        <b-card header="Bills">
            <b-table striped hover :items="bills"></b-table>
        </b-card>
    </b-container>
</template>

<script>
    export default {
        name: "index",
        head: () => ({
            title: 'Bills'
        }),
        data: () => ({
            bills: []
        })
    }
</script>
