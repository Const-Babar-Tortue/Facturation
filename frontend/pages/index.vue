<template>
    <b-container class="mt-5">
        <b-row>
            <b-col>
                <b-jumbotron
                    bg-variant="info"
                    text-variant="white"
                    border-variant="dark"
                    header="Facture Soft"
                    lead="A web app made to organize your bills"
                />
            </b-col>
        </b-row>
    </b-container>
</template>

<script>
export default {
    head: () => ({
        title: 'Home',
    }),
    options: {
        auth: false,
    },
}
</script>
