<template>
    <Centered>
        <b-card header="Create a Bill">
            <ValidationObserver ref="observer" v-slot="{ handleSubmit, valid }">
                <b-form @submit.prevent="handleSubmit(onSubmit)">
                    <DangerAlert
                        :show="exists"
                        msg="A bill with that name already exists"
                    />

                    <DangerAlert
                        :show="error"
                        msg="An error occurred while adding this bill"
                    />

                    <label for="client">Choose a client</label>
                    <b-form-select
                        id="client"
                        v-model="client"
                        name="client"
                        required
                        :options="clients"
                    ></b-form-select>

                    <BTextInputWithValidation
                        v-model="number"
                        rules="required|numeric"
                        label="Number:"
                        name="Number"
                        placeholder="Enter a number"
                    />

                    <label for="date">Choose a date</label>
                    <b-form-datepicker
                        id="date"
                        v-model="date"
                        class="mb-2"
                        required
                    ></b-form-datepicker>

                    <label for="expiration">Choose an expiration date</label>
                    <b-form-datepicker
                        id="expiration"
                        v-model="expiration"
                        class="mb-2"
                        required
                    ></b-form-datepicker>

                    <BTextInputWithValidation
                        v-model="price"
                        rules="required|numeric"
                        label="Price:"
                        name="Price"
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

                    <b-button
                        type="submit"
                        :disabled="!valid"
                        variant="primary"
                    >
                        Submit
                    </b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
import { ValidationObserver } from 'vee-validate'
import '@/validation/rules'

import DangerAlert from '@/components/DangerAlert'
import Centered from '@/components/Centered'
import BTextInputWithValidation from '@/components/inputs/BTextInputWithValidation'

export default {
    name: 'Register',
    components: {
        DangerAlert,
        Centered,
        ValidationObserver,
        BTextInputWithValidation,
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
        clients: [],
    }),
    mounted() {
        this.$axios
            .get('/clients/names')
            .then(({ data }) => (this.clients = data))
    },
    methods: {
        onSubmit() {
            this.exists = false
            this.error = false
            this.register()
        },
        register() {
            this.$axios.post('/bills', {})
        },
    },
    head: () => ({
        title: 'Create bills',
    }),
}
</script>
