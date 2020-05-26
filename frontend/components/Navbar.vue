<template>
    <b-navbar type="dark" variant="primary">
        <b-navbar-brand href="/">FactureSoft</b-navbar-brand>
        <b-navbar-nav>
            <b-nav-item
                v-if="isAuthenticated"
                :active="$route.path.includes('clients')"
                to="/clients"
            >
                Clients
            </b-nav-item>
            <b-nav-item
                v-if="isAuthenticated"
                :active="$route.path.includes('bills')"
                to="/bills"
                >Bills</b-nav-item
            >
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
            <b-nav-form>
                <b-button
                    v-if="isAuthenticated"
                    size="sm"
                    class="my-2 my-sm-0"
                    @click="logout"
                    >Logout</b-button
                >
                <b-button v-else size="sm" class="my-2 my-sm-0" to="/login"
                    >Login</b-button
                >
            </b-nav-form>
        </b-navbar-nav>
    </b-navbar>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    name: 'Navbar',
    computed: {
        ...mapGetters(['isAuthenticated', 'loggedInUser']),
    },
    methods: {
        async logout() {
            await this.$auth.logout()
        },
    },
}
</script>
