<template>
    <Centered>
        <b-card header="Create an account">
            <ValidationObserver ref="observer" v-slot="{ passes }">
                <b-form @submit.prevent="passes(onSubmit)">

                    <b-alert :show="invalid" variant="danger" dismissible class="mt-3">
                        Invalid credentials
                    </b-alert>

                    <b-alert :show="error" variant="danger" dismissible class="mt-3">
                        An error occurred while registering
                    </b-alert>


                    <BTextInputWithValidation
                        rules="required"
                        type="text"
                        label="Username:"
                        name="Username"
                        v-model="username"
                        placeholder="Enter a username"
                    />

                    <BTextInputWithValidation
                        rules="required"
                        name="Password"
                        vid="password"
                        type="password"
                        label="Password"
                        v-model="password"
                        description="We'll never share your password with anyone else"
                        placeholder="Enter password"
                    />

                    <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
    import {extend, ValidationObserver} from "vee-validate";
    import {required} from 'vee-validate/dist/rules';

    import Centered from '@/components/Centered'
    import BTextInputWithValidation from '@/components/BTextInputWithValidation'

    extend('required', {
        ...required,
        message: 'The {_field_} field is required'
    });

    export default {
        name: "Login",
        components: {
            Centered,
            ValidationObserver,
            BTextInputWithValidation
        },
        options: {
            auth: 'guest',
        },
        data: () => ({
            username: null,
            password: null,
            invalid: false,
            error: false
        }),
        methods: {
            onSubmit() {
                this.$auth.loginWith('local', {
                    data: {
                        username: this.username,
                        password: this.password
                    }
                }).then(() => {
                        this.$router.push('/');
                    }
                ).catch(e => {
                    if ((e.response && e.response.status === 401)) this.invalid = true
                    else this.error = true
                })
            },

        }
    }
</script>
