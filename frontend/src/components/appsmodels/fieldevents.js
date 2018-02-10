import Vue from 'vue'

export default new class {

    constructor() {
        this.vue = new Vue()
    }

    activate(field_name) {
        this.vue.$emit('activate', field_name)
    }

    on_activate(callback) {
        this.vue.$on('activate', callback)
    }

    unsubscribe() {
        this.vue.$off('activate')
    }
}
