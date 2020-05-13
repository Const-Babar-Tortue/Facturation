<template>
    <Centered>
        <b-card header="Create an Bill">
            <ValidationObserver ref="observer" v-slot="{ passes }">
                <b-form @submit.prevent="passes(onSubmit)">

                    <b-alert :show="exists" variant="danger" dismissible class="mt-3">
                        A bill with that name already exists
                    </b-alert>

                    <b-alert :show="error" variant="danger" dismissible class="mt-3">
                        An error occurred while add this bill
                    </b-alert>

                    <b-form-select required v-model="client" :options="clients"></b-form-select>

                    <BTextInputWithValidation
                        rules="required"
                        type="number"
                        label="Number:"
                        name="Number"
                        v-model="number"
                        placeholder="Enter a number"
                    />

                    <label for="date">Choose a date</label>
                    <b-form-datepicker id="date" v-model="date" class="mb-2"></b-form-datepicker>

                    <label for="expiration">Choose an expiration date</label>
                    <b-form-datepicker id="expiration" v-model="expiration" class="mb-2"></b-form-datepicker>

                    <BTextInputWithValidation
                        rules="required"
                        type="number"
                        label="Price:"
                        name="Price"
                        v-model="price"
                        placeholder="Enter a price"
                        step=".01"
                    />

                    <b-form-checkbox
                        id="cash"
                        v-model="cash"
                        name="cash"
                        value="paid"
                    >
                        Cash
                    </b-form-checkbox>

                    <b-form-checkbox
                        id="paid"
                        v-model="paid"
                        name="paid"
                        value="paid"
                    >
                        Paid
                    </b-form-checkbox>

                    <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
    import {extend, ValidationObserver} from "vee-validate";
    import {confirmed, email, required} from 'vee-validate/dist/rules';
    import Centered from '@/components/Centered'
    import BTextInputWithValidation from '@/components/BTextInputWithValidation'

    extend('email', {
        ...email,
        message: 'The {_field_} field must be a valid email'
    })
    extend('confirmed', {
        ...confirmed,
        message: 'Both passwords do not match'
    })
    extend('min', {
        validate(value, {length}) {
            return value.length >= length;
        },
        params: ['length'],
        message: 'The {_field_} field must have at least {length} characters'
    })
    extend('required', {
        ...required,
        message: 'The {_field_} field is required'
    });


    export default {
        name: "Register",
        head: () => ({
            title: 'Create bills'
        }),
        components: {
            Centered,
            ValidationObserver,
            BTextInputWithValidation
        },
        data: () => ({
            number: null,
            date: null,
            expiration: null,
            price: null,
            cash: null,
            paid: null,
            client: null,
            exists: false,
            error: false,
            clients: []
        }),
        mounted() {
            this.$axios.get('/clients/names')
                .then(({data}) => this.clients = data)
        },
        methods: {
            onSubmit() {
                this.exists = false
                this.error = false
                this.register()
            },
            register() {
                this.$axios.post('/bills', {

                })
            },

        }
    }
</script>
