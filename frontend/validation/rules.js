import { extend, localize } from 'vee-validate'
import {
    min,
    email,
    numeric,
    required,
    confirmed,
} from 'vee-validate/dist/rules'
import en from 'vee-validate/dist/locale/en.json'

extend('min', min)
extend('email', email)
extend('numeric', numeric)
extend('required', required)
extend('confirmed', confirmed)
localize('en', en)
