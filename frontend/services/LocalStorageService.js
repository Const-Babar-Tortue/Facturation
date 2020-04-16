export function setToken(token) {
    if (process.browser && token) {
        localStorage.setItem('token', token)
    }
}

export function clearToken() {
    if (process.browser) {
        localStorage.removeItem('token')
    }
}

export default {setToken, clearToken}
