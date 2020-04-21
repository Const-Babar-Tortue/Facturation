<template>
    <b-container class="mt-5">
        <b-card header="Clients">
            <b-table striped hover :items="items"></b-table>
        </b-card>
    </b-container>
</template>

<script>
    export default {
        name: "clients",
        data: () => ({
            items: [
                { name: 40, street: 'Dickerson', streetNumber: 'Macdonald', postalCode: 1234, city: 'lln', firm: false, vatNumber: '' },
            ]
        })
    }
</script>
