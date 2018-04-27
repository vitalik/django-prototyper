<template>
    <div class="home">
        <div class="container" style="margin-top: 100px;">
            <div class="row">
                <div class="col-4">
                    <img src="/static/welcome.png" class="img-fluid">
                </div>
                <div class="col">
                    <div v-if="project_apps.length == 0">
                        <h1 class="display-4">Let's get started</h1>
                        <p class="lead">
                            Project <strong>{{ project }}</strong>
                        </p>
                    </div>

                    <div v-if="project_apps.length > 0" class="mb-4">
                        <h1 class="display-4">{{ project }}</h1>
                    </div>


                    <div style="max-width: 300px;">

                        <router-link to="/apps/" class="btn btn-outline-success btn-block">
                            <span v-if="project_apps.length == 0">Create</span>
                            <span v-else>Change</span>
                            apps and models
                        </router-link>
                        <br>
                        <router-link to="/settings/" class="btn btn-outline-success btn-block">Change settings</router-link>
                        <br>
                        <router-link to="/plugins/" class="btn btn-outline-success btn-block">Install some plugins</router-link>
                    </div>
                    
                </div>
            </div>
        </div>
    </div>
</template>

<script>

import _ from 'lodash'
import { store } from '../store'

export default {
    name: 'home',
    computed: {
        project() {
            return store.project.name
        },
        project_apps() {
            return _.filter(store.project.apps, {'external': false})
        }
    }
}
</script>
