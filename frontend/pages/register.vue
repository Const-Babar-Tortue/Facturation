<template>
    <Centered>
        <b-card header="Create an account">
            <ValidationObserver ref="observer" v-slot="{ passes }">
                <b-form @submit.prevent="passes(onSubmit)">

                    <b-alert :show="exists" variant="danger" dismissible class="mt-3">
                        A user with that username or email already exists
                    </b-alert>

                    <b-alert :show="error" variant="danger" dismissible class="mt-3">
                        An error occurred while registering
                    </b-alert>


                    <BTextInputWithValidation
                        rules="required|min:5"
                        type="text"
                        label="Username:"
                        name="Username"
                        v-model="username"
                        placeholder="Enter a username"
                    />

                    <BTextInputWithValidation
                        rules="required|email"
                        type="email"
                        label="Email address:"
                        name="Email"
                        v-model="email"
                        description="We'll never share your email with anyone else"
                        placeholder="Enter email"
                    />

                    <BTextInputWithValidation
                        rules="required|min:6"
                        name="Password"
                        vid="password"
                        type="password"
                        label="Password"
                        v-model="password"
                        description="We'll never share your password with anyone else"
                        placeholder="Enter password"
                    />

                    <BTextInputWithValidation
                        rules="required|confirmed:password"
                        name="Password confirmation"
                        type="password"
                        label="Password confirmation"
                        v-model="confirmation"
                        description="We'll never share your password with anyone else"
                        placeholder="Confirm password"
                    />

                    <b-button type="submit" variant="primary">Submit</b-button>
                </b-form>
            </ValidationObserver>
        </b-card>
    </Centered>
</template>

<script>
    import {ValidationObserver, extend} from "vee-validate";
    import {required, email, confirmed, min} from 'vee-validate/dist/rules';

    // No message specified.
    extend('email', email);
    extend('confirmed', confirmed);
    extend('min', min);
    extend('required', required);

    import Centered from '@/components/Centered'
    import BTextInputWithValidation from '@/components/BTextInputWithValidation'
    import SignupService from '@/services/SignupService.js'

    export default {
        name: "SignupForm",
        components: {
            Centered,
            ValidationObserver,
            BTextInputWithValidation
        },
        data: () => ({
            username: null,
            email: null,
            password: null,
            confirmation: null,
            exists: false,
            error: false
        }),
        methods: {
            onSubmit() {
                this.exists = false
                this.error = false
                this.register()
            },
            register() {
                SignupService.register({
                    username: this.username,
                    email: this.email,
                    password: this.password
                }).then(_ =>
                    this.succeed()
                ).catch(e => {
                    if (e.exists) this.exists = true
                    else this.error = true
                })
            },
            succeed() {
                console.log("yeah")
            }
        }
    }
</script>
