import Vue from 'vue'
import Router from 'vue-router'
import Admin from './components/admin'
import AppsModels from './components/appsmodels'
import Build from './components/build'
import BuildSettings from './components/buildsettings'
import Settings from './components/settings'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/settings/',
            name: 'settings',
            component: Settings
        },
        {
            path: '/buildsettings/',
            name: 'buildsettings',
            component: BuildSettings
        },
        {
            path: '/apps/',
            name: 'appsmodels',
            component: AppsModels
        },
        {
            path: '/admin/',
            name: 'admin',
            component: Admin
        },
        {
            path: '/build/',
            name: 'build',
            component: Build
        },
    ]
})
