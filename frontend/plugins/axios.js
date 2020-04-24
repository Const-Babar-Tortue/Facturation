export default function ({$axios}) {
    $axios.onRequest((config) => {
        console.log('Making request to ' + config.url)
    })

    $axios.setBaseURL(process.env.API_HOST)
}
