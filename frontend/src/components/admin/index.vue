<template>
    <div>
        <h2>Admin</h2>
        <hr>
        
        <div class="row">
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
            </div>
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

<style scoped>
    .djangoapp table tr:first-child td {
        border: none !important;
    }
</style>

