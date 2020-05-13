<template>
    <div>
        <Navbar />
        <b-container fluid="" class="mt-5">
            <nuxt />
        </b-container>
    </div>
</template>

<script>
import Navbar from '~/components/Navbar.vue'

export default {
    components: {
        Navbar,
    },
}
</script>

<style>
body,
html {
    height: 100%;
}
</style>
