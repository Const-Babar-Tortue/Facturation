<template>
<b-card>
    <template v-slot:header>
        <div class="d-flex justify-content-between">
            <span class="my-auto">{{title}}</span>
            <b-btn variant="primary" :to="destination">Create</b-btn>
        </div>
    </template>
    <b-table responsive="" striped hover :items="items"/>
</b-card>
</template>

<script>
    export default {
        name: "DataTable",
        props: {
            title: {
                type: String,
                required: true
            },
            destination: {
                type: String,
                required: true
            },
            items: {
                type: Array,
                required: true
            }
        }
    }
</script>

<style scoped>

</style>
