<template>
    <div class="settings">
        <h2>Django Settings</h2>
        <hr>

        <div class="row">
            <div class="col-5">
                <table>
                    <tr>
                        <th>USE_I18N = </th>
                        <td> <InputTrueFalse v-model.boolean="settings.USE_I18N" class="form-control" /></td>
                    </tr>
                    <tr>
                        <th>USE_L10N = </th>
                        <td> <InputTrueFalse v-model.boolean="settings.USE_L10N" class="form-control" /></td>
                    </tr>
                    <tr>
                        <th>EMAIL_SUBJECT_PREFIX = </th>
                        <td> <input v-model.lazy="settings.EMAIL_SUBJECT_PREFIX" class="form-control"></td>
                    </tr>
                    <tr>
                        <th>ADMIN_SITE_HEADER = </th>
                        <td> <input v-model.lazy="settings.ADMIN_SITE_HEADER" class="form-control"></td>
                    </tr>
                    <tr>
                        <th>DEFAULT_FROM_EMAIL = </th>
                        <td> <input v-model.lazy="settings.DEFAULT_FROM_EMAIL" class="form-control"></td>
                    </tr>
                    <tr>
                        <th>TIME_ZONE = </th>
                        <td> <input v-model.lazy="settings.TIME_ZONE" class="form-control"></td>
                    </tr>
                    <tr>
                        <th>LANGUAGE_CODE = </th>
                        <td> <input v-model.lazy="settings.LANGUAGE_CODE" class="form-control"></td>
                    </tr>
                </table>
            </div>
            <div class="col-3">
                <h5>Django contib apps:</h5>
                <button v-for="app in django_apps"
                    @click="toggle_app(app)"
                    :key="app.name"
                    :class="{'btn-primary': app.selected, 'btn-secondary': !app.selected}" 
                    class="btn btn-block btn-sm text-left">
                        django.contrib.{{app.name}}
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import { DJANGO_CONTRIB_APPS } from '../../django/apps'
import InputTrueFalse from '../utils/InputTrueFalse'

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
    components: {
        InputTrueFalse,
    }
}
</script>

<style lang="scss">

.settings {
    table th {
        font-weight: normal;
        text-align: right;
        padding-right: 4px;
    }
}

</style>
