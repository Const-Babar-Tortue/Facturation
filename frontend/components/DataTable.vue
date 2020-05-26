<template>
    <b-card no-body>
        <template v-slot:header>
            <div class="d-flex justify-content-between">
                <div class="my-auto">
                    <span class="my-auto">{{ title }}</span>
                    <b-badge pill class="my-auto">{{ items.length }}</b-badge>
                </div>
                <b-btn variant="primary" :to="destination">Create</b-btn>
            </div>
        </template>
        <b-table
            class="m-0"
            responsive=""
            striped
            hover
            :items="items"
            :fields="fields"
        />
    </b-card>
</template>

<script>
export default {
    name: 'DataTable',
    props: {
        title: {
            type: String,
            required: true,
        },
        destination: {
            type: String,
            required: true,
        },
        items: {
            type: Array,
            required: true,
        },
        fields: {
            type: Array,
            required: true,
        },
    },
}
</script>

<style scoped></style>
