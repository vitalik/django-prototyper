import Vue from 'vue'
import Prototyper from './Prototyper.vue'


import router from './router'
import VueRouter from 'vue-router'
Vue.use(VueRouter)


require('./assets/bootstrap_custom.scss');
require('./assets/styles.scss');

new Vue({
    el: '#prototyper',
    router,
    render: h => h(Prototyper)
})
