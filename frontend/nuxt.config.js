export default {
    mode: 'universal',
    /*
    ** Headers of the page
    */
    head: {
        title: 'Bills',
        meta: [
            {charset: 'utf-8'},
            {name: 'viewport', content: 'width=device-width, initial-scale=1'},
            {hid: 'description', name: 'description', content: process.env.npm_package_description || ''}
        ],
        link: [
            {rel: 'icon', type: 'image/x-icon', href: '/favicon.ico'}
        ]
    },
    /*
    ** Customize the progress-bar color
    */
    loading: {color: '#fff'},
    /*
    ** Global CSS
    */
    css: [
        '~/assets/main.css'
    ],
    /*
    ** Plugins to load before mounting the App
    */
    plugins: ['~/plugins/nuxt-client-init.client.js'],
    /*
    ** Nuxt.js dev-modules
    */
    buildModules: [],
    /*
    ** Nuxt.js modules
    */
    modules: [
        // Doc: https://bootstrap-vue.js.org
        'bootstrap-vue/nuxt',
        '@nuxtjs/axios'
    ],
    /*
    ** Build configuration
    */
    build: {
        // Add exception
        transpile: [
            "vee-validate/dist/rules",
            'vee-validate'
        ],
        /*
        ** You can extend webpack config here
        */
        extend(config, ctx) {
        }
    }
}
