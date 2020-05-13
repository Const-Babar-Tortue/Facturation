<template>
    <div class="h-100">
        <Navbar/>
        <nuxt/>
    </div>
</template>

<script>
    import Navbar from '~/components/Navbar.vue'

    export default {
        components: {
            Navbar
        }
    }
</script>

<style>
    body,html {
        height: 100%;
    }
</style>
