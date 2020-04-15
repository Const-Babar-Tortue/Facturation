export function setToken(token) {
    if (process.browser) {
        localStorage.setItem('token', token)
    }
}

// should only be run at initialization, use VueX store after
export function getToken() {
    if (process.browser) {
        return localStorage.getItem('token')
    }
    return null
}

export function clearToken() {
    if (process.browser) {
        localStorage.removeItem('token')
    }
}

export default {setToken, getToken, clearToken}
