<template>
    <div id="app">
        <nav class="navbar navbar-light bg-white justify-content-between">
            <span class="navbar-text">
                <span class="branding mr-2">
                    <img src="/static/logo.png" style="width: 25px; height: 24px;">
                    Prototyper
                </span>
                {{ project.name }}
                 
                <span v-if="is_saving" class="badge badge-warning">Saving...</span>
            </span>
            <div style="width: 30%;">
                <router-link class="btn btn-danger my-2 my-sm-0 float-right" to="/build/">
                    <i class="fas fa-rocket"></i>
                    Build
                </router-link>

                <validation-icon class="float-right mr-2"></validation-icon>
            </div>
        </nav>

        <div id="sidebar" class="pt-2">
            <div class="nav flex-column nav-pills">
                <router-link to="/" class="nav-link" :class="{'active':$route.path == '/'}">Home</router-link>
                <router-link to="/buildsettings/" class="nav-link" active-class="active">Build Settings</router-link>
                <router-link to="/settings/" class="nav-link" active-class="active">Django Settings</router-link>
                <router-link to="/apps/" class="nav-link" active-class="active">Apps / Models</router-link>
                <router-link to="/admin/" class="nav-link" active-class="active">Admin</router-link>
                <router-link to="/plugins/" class="nav-link" active-class="active">Plugins</router-link>
            </div>
        </div>

        <div id="maincontent">
            <router-view></router-view>
        </div>

    </div>
</template>

<script>

import { store } from './store'
import ValidationIcon from './components/build/ValidationIcon.vue'

export default {
    name: 'prototyper',
    data () {
        return {
            project: store.project,
            is_saving: false,
        }
    },
    watch: {
        project: {
            deep: true,
            handler(val, old) {
                this.is_saving = true
                //TODO: I guess debaunce should be here better
                store.save().then((response) => {
                    setTimeout(()=> { this.is_saving = false }, 300)
                })
            }
        }
    },
    components: {
        ValidationIcon,
    }
}
</script>
