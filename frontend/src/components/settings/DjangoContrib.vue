<template>

    <div class="django-contrib">
        <h5>Django contib apps:</h5>
        <div class="row">
            <div class="col-6">
                <code>INSTALLED_APPS = [</code>
                <button v-for="app in selected_apps"
                    @click="toggle_app(app)"
                    :key="app.name"
                    class="btn btn-primary btn-block btn-sm text-left ml-3">
                        <span class="float-right"><i class="fas fa-trash-alt"></i></span>
                        django.contrib.{{app.name}} 
                </button>
                &nbsp; ...<br>
                <code>]</code>
            </div>
            <div class="col-6">
                Available
                <button v-for="app in availalbe_apps"
                    @click="toggle_app(app)"
                    :key="app.name"
                    class="btn btn-secondary btn-block btn-sm text-left ml-1">
                        <i class="fas fa-plus mr-1"></i> django.contrib.{{app.name}}
                </button>
            </div>
        </div>

    </div>

</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import { DJANGO_CONTRIB_APPS } from '../../django/apps'

export default {
    name: 'settings',
    data() {
        return {
            settings: store.project.settings
        }
    },
    computed: {
        django_apps() {
            return _.map(_.keys(DJANGO_CONTRIB_APPS), (app) => {
                return {
                    'name': app,
                    'selected': (store.app_get(app) !== undefined),
                }
            })
        },
        availalbe_apps() {
            return _.filter(this.django_apps, {'selected': false})
        },
        selected_apps() {
            return _.filter(this.django_apps, {'selected': true})
        }
    },
    methods: {
        toggle_app(app) {
            if (app.selected) {
                store.app_delete(app.name)
            } else {
                store.apps_add_django(app.name)
            }
        }
    },
}
</script>
