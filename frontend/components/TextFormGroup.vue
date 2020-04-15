<template>
    <div>
        <b-form-group :id="id + '-group'" :label="label" :label-for="id">
            <b-form-input
                :id="id"
                v-model="innerValue"
                :type="type"
            ></b-form-input>
            <b-form-invalid-feedback :state="valid">
            </b-form-invalid-feedback>
        </b-form-group>
    </div>

</template>

<script>
    export default {
        name: "TextFormGroup",
        props: {
            id: {
                type: String,
                required: true
            },
            label: {
                type: String,
                required: true
            },
            valid: {
                type: Boolean,
                required: false,
                default: true
            },
            value: {
                type: null
            },
            type: {
                type: String,
                default: 'text'
            }
        },
        data: () => ({
            innerValue: null
        }),
        watch: {
            innerValue(value) {
                this.$emit('input', value)
            },
            value(value) {
                this.innerValue = value
            }
        },
        created() {
            if (this.value) {
                this.innerValue = this.value
            }
        }
    }
</script>
