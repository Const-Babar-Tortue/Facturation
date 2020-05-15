module.exports = {
    'Test title'(browser) {
        browser
            .url('http://127.0.0.1:3002')
            .waitForElementVisible('body')
            .assert.titleContains('facturesoft')
            .end()
    },

    'Test login with invalid credentials'(browser) {
        browser
            .url('http://127.0.0.1:3002/login')
            .waitForElementVisible('body')
            .setValue('input[name=Username]', 'babar')
            .setValue('input[name=Password]', 'michel')
            .assert.visible('button[type=submit]')
            .click('button[type=submit]')
            .assert.visible('.alert')
            .assert.containsText('.alert', 'Invalid credentials')
            .end()
    },
}
