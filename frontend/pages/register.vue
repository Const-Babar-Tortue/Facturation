<template>
    <Centered>
        <b-card header="Create an account">
            <ValidationObserver ref="observer" v-slot="{ passes }">
                <b-form @submit.prevent="passes(onSubmit)">
                    <b-alert
                        :show="exists"
                        variant="danger"
                        dismissible
                        class="mt-3"
                    >
                        A user with that username or email already exists
                    </b-alert>

                    <b-alert
                        :show="error"
                        variant="danger"
                        dismissible
                        class="mt-3"
                    >
                        An error occurred while registering
                    </b-alert>

                    <BTextInputWithValidation
                        v-model="username"
                        rules="required|min:5"
                        type="text"
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

                    <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
import { extend, ValidationObserver } from 'vee-validate'
import { confirmed, email, required } from 'vee-validate/dist/rules'
import Centered from '@/components/Centered'
import BTextInputWithValidation from '@/components/BTextInputWithValidation'

extend('email', {
    ...email,
    message: 'The {_field_} field must be a valid email',
})
extend('confirmed', {
    ...confirmed,
    message: 'Both passwords do not match',
})
extend('min', {
    validate(value, { length }) {
        return value.length >= length
    },
    params: ['length'],
    message: 'The {_field_} field must have at least {length} characters',
})
extend('required', {
    ...required,
    message: 'The {_field_} field is required',
})

export default {
    name: 'Register',
    components: {
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
