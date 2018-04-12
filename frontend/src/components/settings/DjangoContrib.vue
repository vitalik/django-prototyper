<template>

    <div class="django-contrib">
        <h5>Django contib apps:</h5>
        <div class="row">
            <div class="col-6">
                INSTALLED_APPS = [
                <button v-for="app in selected_apps"
                    @click="toggle_app(app)"
                    :key="app.name"
                    class="btn btn-primary btn-block btn-sm text-left ml-3">
                        django.contrib.{{app.name}} <span class="float-right">></span>
                </button>
                &nbsp; ...<br>
                ]
            </div>
            <div class="col-6">
                Available
                <button v-for="app in availalbe_apps"
                    @click="toggle_app(app)"
                    :key="app.name"
                    class="btn btn-secondary btn-block btn-sm text-left ml-1">
                        < django.contrib.{{app.name}}
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
