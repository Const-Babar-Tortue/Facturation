<template>
    <Centered>
        <b-card header="Create an client">
            <ValidationObserver ref="observer" v-slot="{ passes }">
                <b-form @submit.prevent="passes(onSubmit)">

                    <b-alert :show="exists" variant="danger" dismissible class="mt-3">
                        A client with that name already exists
                    </b-alert>

                    <b-alert :show="error" variant="danger" dismissible class="mt-3">
                        An error occurred while add this client
                    </b-alert>

                    <BTextInputWithValidation
                        rules="required|min:5"
                        type="text"
                        label="Name:"
                        name="Name"
                        v-model="name"
                        placeholder="Enter a name"
                    />

                    <BTextInputWithValidation
                        rules="required"
                        type="text"
                        label="Street:"
                        name="Street"
                        v-model="street"
                        placeholder="Enter a street"
                    />

                    <BTextInputWithValidation
                        rules="required"
                        type="text"
                        label="Number:"
                        name="Number"
                        v-model="number"
                        placeholder="Enter a street number"
                    />

                    <BTextInputWithValidation
                        rules="required"
                        type="number"
                        label="Postal code:"
                        name="Postal"
                        v-model="postal"
                        placeholder="Enter a postal code"
                    />

                    <BTextInputWithValidation
                        rules="required"
                        type="text"
                        label="City:"
                        name="City"
                        v-model="city"
                        placeholder="Enter a city"
                    />

                    <b-form-checkbox
                        id="firm"
                        v-model="firm"
                        name="firm"
                        value="true"
                    >
                        firm
                    </b-form-checkbox>

                    <BTextInputWithValidation
                        rules="required"
                        type="text"
                        label="VAT:"
                        name="Vat"
                        v-model="vat"
                        placeholder="Enter a Vat number"
                    />

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
        components: {
            Centered,
            ValidationObserver,
            BTextInputWithValidation
        },
        data: () => ({
            name: null,
            street: null,
            number: null,
            postal: null,
            city: null,
            firm: null,
            vat: null,
            exists: false,
            error: false
        }),
        methods: {
            onSubmit() {
                this.exists = false
                this.error = false
                this.createClient()
            },
            createClient() {
               /* ClientService.createClient({
                    name: this.name,
                    street: this.street,
                    streetNumber: this.number,
                    postalCode: this.postal,
                    city: this.city,
                    firm: !!this.firm,
                    vatNumber: this.vat
                }).then(_ =>
                    this.$router.push('/clients')
                ).catch(e => {
                    if (e.exists) this.exists = true
                    else this.error = true
                }) */
            },

        }
    }
</script>
