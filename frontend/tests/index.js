require('dotenv').config()

const username = process.env.USERNAME
const password = process.env.PASSWORD

const faker = require('faker')
faker.locale = 'fr'
const companyName = faker.company.companyName()

const baseUrl = 'http://127.0.0.1:3000'
// const baseUrl = 'https://facturesoft.ovh'

module.exports = {
    after: (browser) => {
        browser.end()
    },
    before: (browser) => {
        browser.url(baseUrl).waitForElementVisible('body')
    },

    'Test title'(browser) {
        browser.assert.titleContains('facturesoft')
    },

    'Test invalid login'(browser) {
        browser
            .url(`${baseUrl}/login`)
            .waitForElementVisible('body')
            .setValue('input[name=Username]', 'babar')
            .setValue('input[name=Password]', 'michel')
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.visible('.alert')
            .assert.containsText('.alert', 'Invalid credentials')
    },

    'Test valid login'(browser) {
        browser
            .clearValue('input[name=Username]')
            .clearValue('input[name=Password]')
            .setValue('input[name=Username]', username)
            .setValue('input[name=Password]', password)
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.not.elementPresent('.alert')
            .assert.urlEquals(`${baseUrl}/`)
            .assert.containsText('button[type=button]', 'Logout')
            .assert.containsText('a[href="/clients"]', 'Clients')
            .assert.containsText('a[href="/bills"]', 'Bills')
            .click('a[href="/clients"]')
            .assert.urlEquals(`${baseUrl}/clients`)
    },

    'Test clients list'(browser) {
        browser
            .click('a[href="/clients"]')
            .assert.urlEquals(`${baseUrl}/clients`)
    },

    'Test client creation'(browser) {
        browser
            .click('a[href="/clients/create"]')
            .assert.urlEquals(`${baseUrl}/clients/create`)
            .setValue('input[name=Name]', companyName)
            .setValue('input[name=Street]', faker.address.streetName())
            .setValue('input[name=Number]', '123')
            .setValue('input[name=Postal]', faker.address.zipCode())
            .setValue('input[name=City]', faker.address.city())
            .setValue('input[name=Vat]', faker.finance.iban())
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.urlEquals(`${baseUrl}/clients`)
            .assert.containsText('tbody', companyName)
    },
}
