<template>
    <div id="app">
        <nav class="navbar navbar-dark bg-dark justify-content-between">
            <span class="navbar-text">
                <span  class="badge badge-light" style="font-size: 1.1rem; font-weight: 100">Prototyper</span>
                &nbsp;
                {{ project.name }}
                 
                <span v-if="is_saving" class="badge badge-warning">Saving...</span>
            </span>
            <router-link class="btn btn-outline-light my-2 my-sm-0" to="/build/">
                <i class="fas fa-rocket"></i>
                Build
            </router-link>
            
        </nav>
        <div class="container-fluid h-100">
            <div class="row h-100">
                <div class="col-3 col-lg-2 column siebar h-100">
                    <div class="nav flex-column nav-pills">
                        <router-link to="/buildsettings/" class="nav-link" active-class="active">Build Settings</router-link>
                        <router-link to="/settings/" class="nav-link" active-class="active">Django Settings</router-link>
                        <router-link to="/apps/" class="nav-link" active-class="active">Apps / Models</router-link>
                        <router-link to="/admin/" class="nav-link" active-class="active">Admin</router-link>
                    </div>
                </div>
                <div class="col-9 col-lg-10 column h-100">
                    <router-view></router-view>
                </div>
            </div>
            
        </div>
        
    </div>
</template>

<script>

import { store } from './store'

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
                store.save().then((response) => {
                    setTimeout(()=> { this.is_saving = false }, 300)
                })
            }
        }
    }
}
</script>
