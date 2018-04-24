<template>
    <div>
        <table class="table table-sm" @mouseout="mouse_over_app = null">
        <thead>
            <tr>
                <th class="border-0">app</th><th class="border-0" colspan="2">color</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="app in apps" @mouseover="mouse_over_app = app.name">
                <td>{{ app.name }}</td>
                <td>
                    <button :style="{'background-color': app.ui_color}" class="btn btn-sm border mr-1 ml-2">&nbsp; &nbsp;</button>
                </td>
                <td :style="{opacity: mouse_over_app == app.name ? 1 : 0}">
                    <button v-for="color in colors" 
                        :style="{'background-color': color}" 
                        :class="{'border-dark': color == app.ui_color}"
                        @click="app.ui_color = color"
                        class="btn btn-sm border mr-1">
                            &nbsp; &nbsp;
                    </button>
                </td>
            </tr>
        </tbody>
        </table>
    </div>
</template>

<script>

import _ from 'lodash'
import { store } from '../../../store'
import { APP_COLORS } from './colors'


export default {
    name: 'AppColors',
    data() {
        return {
            mouse_over_app: null,
        }
    },
    computed: {
        apps() {
            let apps = _.filter(store.project.apps, a => a.models.length > 0)
            return _.sortBy(apps, ['name'])
        },
        colors() {
            return APP_COLORS
        }
    },

}
</script>
