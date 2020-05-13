export default function ({ $axios }) {
    $axios.setBaseURL(process.env.API_HOST)
}
