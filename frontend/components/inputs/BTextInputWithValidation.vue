<template>
    <ValidationProvider
        v-slot="{ valid, errors }"
        :vid="vid"
        :name="$attrs.name"
        :rules="rules"
    >
        <b-form-group v-bind="$attrs">
            <b-form-input
                v-model="innerValue"
                v-bind="$attrs"
                :state="errors[0] ? false : valid ? true : null"
            ></b-form-input>
            <b-form-invalid-feedback id="inputLiveFeedback">{{
                errors[0]
            }}</b-form-invalid-feedback>
        </b-form-group>
    </ValidationProvider>
</template>

<script>
import { ValidationProvider } from 'vee-validate'

export default {
    components: {
        ValidationProvider,
    },
    props: {
        vid: {
            type: String,
            default: '',
        },
        rules: {
            type: [Object, String],
            default: '',
        },
    },
    data: () => ({
        innerValue: '',
    }),
    watch: {
        // Handles internal model changes.
        innerValue(newVal) {
            this.$emit('input', newVal)
        },
        // Handles external model changes.
        value(newVal) {
            this.innerValue = newVal
        },
    },
    created() {
        if (this.value) {
            this.innerValue = this.value
        }
    },
}
</script>
