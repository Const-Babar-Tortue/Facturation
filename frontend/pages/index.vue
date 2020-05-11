<template>
    <b-container class="mt-5">
        <b-row>
            <b-col>
                <b-jumbotron header="Facturation" lead="blablabla">
                    <p>blablabla</p>
                    <b-button variant="primary" to="/bills">Bills</b-button>
                </b-jumbotron>
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
    export default {
        options: {
            auth: false,
        },
    }
</script>
