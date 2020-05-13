<template>
    <Centered>
        <b-card header="Create an account">
            <ValidationObserver ref="observer" v-slot="{ handleSubmit, valid }">
                <b-form @submit.prevent="handleSubmit(onSubmit)">
                    <DangerAlert
                        :show="exists"
                        msg="A user with that username or email already exists"
                    />

                    <DangerAlert
                        :show="error"
                        msg="An error occurred while registering"
                    />

                    <BTextInputWithValidation
                        v-model="username"
                        rules="required|min:5"
                        label="Username:"
                        name="Username"
                        placeholder="Enter a username"
                    />

                    <BTextInputWithValidation
                        v-model="email"
                        rules="required|email"
                        type="email"
                        label="Email address:"
                        name="Email"
                        description="We'll never share your email with anyone else"
                        placeholder="Enter email"
                    />

                    <BTextInputWithValidation
                        v-model="password"
                        rules="required|min:6"
                        name="Password"
                        vid="password"
                        type="password"
                        label="Password"
                        description="We'll never share your password with anyone else"
                        placeholder="Enter password"
                    />

                    <BTextInputWithValidation
                        v-model="confirmation"
                        rules="required|confirmed:password"
                        name="Password confirmation"
                        type="password"
                        label="Password confirmation"
                        placeholder="Confirm password"
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
        username: null,
        email: null,
        password: null,
        confirmation: null,
        exists: false,
        error: false,
    }),
    methods: {
        onSubmit() {
            this.exists = false
            this.error = false
            this.register()
        },
        register() {
            this.$axios
                .post('/register', {
                    username: this.username,
                    email: this.email,
                    password: this.password,
                })
                .then((_) => this.$router.push('/'))
                .catch((e) => {
                    if (e.response && e.response.status === 409)
                        this.exists = true
                    else this.error = true
                })
        },
    },
    head: () => ({
        title: 'Register',
    }),
    options: {
        auth: false,
    },
}
</script>
