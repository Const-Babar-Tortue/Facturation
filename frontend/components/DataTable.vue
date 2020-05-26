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

        <b-modal id="modal" hide-footer>
            <div class="d-block text-center">
                <h3>Are you sure ?</h3>
            </div>
            <b-button variant="danger" class="mt-3" block @click="confirm"
                >I'm sure</b-button
            >
            <b-button class="mt-3" block @click="cancel">Cancel</b-button>
        </b-modal>

        <b-table
            class="m-0"
            responsive=""
            striped
            hover
            :items="items"
            :fields="fields"
        >
            <template v-slot:cell(actions)="row">
                <b-button size="sm" @click="askForDeletion(row.item)">
                    Delete
                </b-button>
            </template>
        </b-table>
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
        deleteItem: {
            type: Function,
            required: true,
        },
    },
    data: () => ({
        selectedItem: null,
    }),
    methods: {
        askForDeletion(item) {
            this.selectedItem = item
            this.$bvModal.show('modal')
        },
        confirm() {
            this.$bvModal.hide('modal')
            this.deleteItem(this.selectedItem)
        },
        cancel() {
            this.$bvModal.hide('modal')
            this.selectedItem = null
        },
    },
}
</script>
