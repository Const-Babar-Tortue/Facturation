<template>
    <b-alert :show="show" variant="danger" dismissible>
        {{ msg }}
    </b-alert>
</template>
<script>
export default {
    name: 'DangerAlert',
    props: {
        show: Boolean,
        msg: {
            type: String,
            required: true,
        },
    },
}
</script>
