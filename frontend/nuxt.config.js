const env = require('dotenv').config().parsed

export default ({ dev }) => {
    return {
        mode: 'universal',
        /*
         ** Headers of the page
         */
        head: {
            titleTemplate: '%s - facturesoft',
            title: 'facturesoft',
            htmlAttrs: {
                lang: 'en',
            },
            meta: [
                { charset: 'utf-8' },
                {
                    name: 'viewport',
                    content: 'width=device-width, initial-scale=1',
                },
                {
                    hid: 'description',
                    name: 'description',
                    content: process.env.npm_package_description || '',
                },
            ],
            link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
        },
        /*
         ** Customize the progress-bar color
         */
        loading: { color: '#fff' },
        /*
         ** Global CSS
         */
        css: ['~/assets/main.css'],
        /*
         ** Plugins to load before mounting the App
         */
        plugins: ['~/plugins/axios.js'],
        /*
         ** Nuxt.js dev-modules
         */
        buildModules: ['@nuxtjs/dotenv'],
        /*
         ** Nuxt.js modules
         */
        modules: [
            // Doc: https://bootstrap-vue.js.org
            'bootstrap-vue/nuxt',
            '@nuxtjs/axios',
            '@nuxtjs/auth',
        ],
        /*
         ** Build configuration
         */
        build: {
            // Add exception
            transpile: ['vee-validate/dist/rules', 'vee-validate'],
            /*
             ** You can extend webpack config here
             */
            extend(config, ctx) {},
        },

        env: {
            API_HOST: env.API_HOST,
        },

        router: {
            middleware: ['auth'],
        },

        auth: {
            redirect: {
                login: '/login',
                logout: '/',
                home: '/',
                callback: false,
            },
            watchLoggedIn: true,
            cookie: dev, // only use cookies in development
            strategies: {
                local: {
                    endpoints: {
                        login: {
                            url: '/auth',
                            method: 'post',
                            propertyName: 'access_token',
                        },
                        user: {
                            url: '/user/me',
                            method: 'get',
                            propertyName: 'user',
                        },
                    },
                    autoFetchUser: true,
                },
            },
        },
    }
}
