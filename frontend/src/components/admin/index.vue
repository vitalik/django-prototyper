<template>
    <div class="admin">
        <div class="heading">
            <div class="container-fluid">
                <h2>Admin</h2>
            </div>
        </div>

        <div class="col-md-6 col-lg-4">
            <div v-for="app in apps" class="card djangoapp mb-1">
                <strong class="card-header">{{app.name}}</strong>
                <div  class="card-body">
                    <table class="table table-sm table-hover">

                        <tr v-for="model in app.models">
                            <td :class="{'text-muted':!model.admin.generate}">
                                <input type="checkbox" v-model.boolean="model.admin.generate" class="mr-2">

                                <router-link v-if="model.admin.generate" :to="{name: 'admin-edit', params: {app: app.name, model:model.name}}">
                                    {{model.name}}
                                </router-link>
                                <span v-else class="text-muted">{{model.name}}</span>
                            </td>
                        </tr>
                    </table>
                </div>
            </div>
            

            <div v-if="apps.length == 0">
                You do not have any apps yet.
                <router-link to="/apps/">Go to apps and models</router-link> to create some.
            </div>
        </div>

    </div>

</template>

<script>

import { store } from '../../store'

export default {
    name: 'admin',
    computed: {
        apps() {
            let apps = _.filter(store.project.apps, {'external': false})
            return _.sortBy(apps, ['name'])
        }
    },

}

</script>


