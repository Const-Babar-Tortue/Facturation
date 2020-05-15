require('dotenv').config()
const username = process.env.USERNAME
const password = process.env.PASSWORD

// const baseUrl = 'http://127.0.0.1:3002'
const baseUrl = 'https://facturesoft.ovh'

module.exports = {
    'Test title'(browser) {
        browser
            .url(baseUrl)
            .waitForElementVisible('body')
            .assert.titleContains('facturesoft')
            .end()
    },

    'Test login with invalid credentials'(browser) {
        browser
            .url(`${baseUrl}/login`)
            .waitForElementVisible('body')
            .setValue('input[name=Username]', 'babar')
            .setValue('input[name=Password]', 'michel')
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.visible('.alert')
            .assert.containsText('.alert', 'Invalid credentials')
            .end()
    },

    'Test login with valid credentials'(browser) {
        browser
            .url(`${baseUrl}/login`)
            .waitForElementVisible('body')
            .setValue('input[name=Username]', username)
            .setValue('input[name=Password]', password)
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.not.elementPresent('.alert')
            .assert.urlEquals(`${baseUrl}/`)
            .assert.containsText('button[type=button]', 'Logout')
            .assert.containsText('a[href="/clients"]', 'Clients')
            .assert.containsText('a[href="/bills"]', 'Bills')
            .end()
    },
}
