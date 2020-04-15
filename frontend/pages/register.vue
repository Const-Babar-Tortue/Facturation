<template>
    <Centered>
        <b-card header="Create an account">
            <b-form @submit.prevent="handleSubmit">

                <b-alert :show="exists" variant="danger" dismissible class="mt-3">
                    A user with that username or email already exists
                </b-alert>

                <b-alert :show="error" variant="danger" dismissible class="mt-3">
                    An error occurred while registering
                </b-alert>

                <TextFormGroup
                    id="username"
                    label="Username:"
                    v-model="form.username"
                />
                <TextFormGroup
                    id="email"
                    label="Email:"
                    v-model="form.email"
                />
                <TextFormGroup
                    id="password"
                    label="Password:"
                    v-model="form.password"
                    type="password"
                />
                <TextFormGroup
                    id="repeat-password"
                    label="Repeat password:"
                    v-model="form.repeatPassword"
                    type="password"
                />

                <b-button type="submit" variant="primary">Submit</b-button>
            </b-form>

        </b-card>
    </Centered>
</template>

<script>
    // import Api from '@/api'
    import Centered from '@/components/Centered'
    import TextFormGroup from '@/components/TextFormGroup'
    import SignupService from '@/services/SignupService.js'

    export default {
        name: "SignupForm",
        components: {
            Centered,
            TextFormGroup
        },
        data: () => ({
            form: {
                username: null,
                email: null,
                password: null,
                repeatPassword: null,
            },
            exists: false,
            error: false
        }),
        methods: {
            handleSubmit() {
                this.exists = false
                this.error = false
                // TODO: validate
                if (true) this.register()
            },
            register() {


                SignupService.register({
                    username: this.form.username,
                    email: this.form.email,
                    password: this.form.password
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
