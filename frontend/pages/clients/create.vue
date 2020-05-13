<template>
    <Centered>
        <b-card header="Create a client">
            <ValidationObserver ref="observer" v-slot="{ handleSubmit, valid }">
                <b-form @submit.prevent="handleSubmit(onSubmit)">
                    <DangerAlert
                        :show="exists"
                        msg="A client with that name already exists"
                    />

                    <DangerAlert
                        :show="error"
                        msg="An error occurred while add this client"
                    />

                    <BTextInputWithValidation
                        v-model="name"
                        rules="required|min:3"
                        label="Name:"
                        name="Name"
                        placeholder="Enter a name"
                    />

                    <BTextInputWithValidation
                        v-model="street"
                        rules="required|min:3"
                        label="Street:"
                        name="Street"
                        placeholder="Enter a street"
                    />

                    <BTextInputWithValidation
                        v-model="number"
                        rules="required|min:3"
                        label="Number:"
                        name="Number"
                        placeholder="Enter a street number"
                    />

                    <BTextInputWithValidation
                        v-model="postal"
                        rules="required|numeric|min:3"
                        label="Postal code:"
                        name="Postal"
                        placeholder="Enter a postal code"
                    />

                    <BTextInputWithValidation
                        v-model="city"
                        rules="required|min:3"
                        label="City:"
                        name="City"
                        placeholder="Enter a city"
                    />

                    <BTextInputWithValidation
                        v-model="vat"
                        rules="required"
                        label="VAT:"
                        name="Vat"
                        placeholder="Enter a Vat number"
                    />

                    <b-form-group>
                        <b-form-checkbox
                            id="firm"
                            v-model="firm"
                            name="firm"
                            value="true"
                            >firm
                        </b-form-checkbox>
                    </b-form-group>

                    <b-button type="submit" :disabled="!valid" variant="primary"
                        >Submit
                    </b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import '@/validation/rules'

import Centered from '@/components/Centered'
import BTextInputWithValidation from '@/components/inputs/BTextInputWithValidation'
import DangerAlert from '@/components/DangerAlert'

export default {
    name: 'Register',
    components: {
        DangerAlert,
        Centered,
        ValidationObserver,
        BTextInputWithValidation,
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
        error: false,
    }),
    methods: {
        onSubmit() {
            this.exists = false
            this.error = false
            this.createClient()
        },
        createClient() {
            this.$axios
                .post('/clients', {
                    name: this.name,
                    street: this.street,
                    streetNumber: this.number,
                    postalCode: this.postal,
                    city: this.city,
                    firm: !!this.firm,
                    vatNumber: this.vat,
                })
                .then((_) => this.$router.push('/clients'))
                .catch((e) => {
                    if (e.response && e.response.status === 409)
                        this.exists = true
                    else this.error = true
                })
        },
    },
    head: () => ({
        title: 'Create clients',
    }),
}
</script>
