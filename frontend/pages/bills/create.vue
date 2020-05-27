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
                        v-model="subject"
                        rules="required|min:3"
                        label="Subject:"
                        name="Subject"
                        placeholder="Enter a subjet"
                        step=".01"
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
        subject: null,
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
        this.$axios.get('/clients/names').then(
            ({ data }) =>
                (this.clients = data.map((e) => ({
                    value: e.id,
                    text: e.name,
                })))
        )
    },
    methods: {
        onSubmit() {
            this.exists = false
            this.error = false
            this.register()
        },
        register() {
            this.$axios
                .post('/bills', {
                    clientId: this.client,
                    date: this.date,
                    expiration: this.expiration,
                    price: this.price,
                    cash: !!this.cash,
                    paid: !!this.paid,
                    subject: this.subject,
                })
                .then((_) => this.$router.push('/bills'))
                .catch((e) => {
                    if (e.response && e.response.status === 409)
                        this.exists = true
                    else this.error = true
                })
        },
    },
    head: () => ({
        title: 'Create bills',
    }),
}
</script>
