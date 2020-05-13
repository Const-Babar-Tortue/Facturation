<template>
    <Centered>
        <b-card header="Login">
            <ValidationObserver ref="observer" v-slot="{ handleSubmit, valid }">
                <b-form @submit.prevent="handleSubmit(onSubmit)">
                    <DangerAlert :show="invalid" msg="Invalid credentials" />

                    <DangerAlert
                        :show="error"
                        msg="An error occurred while logging in"
                    />

                    <BTextInputWithValidation
                        v-model="username"
                        rules="required"
                        label="Username:"
                        name="Username"
                        placeholder="Enter a username"
                    />

                    <BTextInputWithValidation
                        v-model="password"
                        rules="required"
                        name="Password"
                        vid="password"
                        type="password"
                        label="Password"
                        placeholder="Enter password"
                    />

                    <b-button type="submit" :disabled="!valid" variant="primary"
                        >Submit</b-button
                    >
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
    name: 'Login',
    components: {
        DangerAlert,
        Centered,
        ValidationObserver,
        BTextInputWithValidation,
    },
    data: () => ({
        username: null,
        password: null,
        invalid: false,
        error: false,
    }),
    methods: {
        onSubmit() {
            this.$auth
                .loginWith('local', {
                    data: {
                        username: this.username,
                        password: this.password,
                    },
                })
                .then(() => {
                    this.$router.push('/')
                })
                .catch((e) => {
                    if (e.response && e.response.status === 401)
                        this.invalid = true
                    else this.error = true
                })
        },
    },
    head: () => ({
        title: 'Login',
    }),
    options: {
        auth: 'guest',
    },
}
</script>
