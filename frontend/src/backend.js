import axios from "axios"

var request = axios.create({
    baseURL: '/api/'
})

request.defaults.xsrfCookieName = 'csrftoken'
request.defaults.xsrfHeaderName = 'X-CSRFToken'


export default {
    build(body) {
        return request.post('/build/', body)
    },
    save(project) {
        return request.post('/save/', project)
    },
}
