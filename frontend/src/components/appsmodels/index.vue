<template>
    <div>
        <h2>Apps and Models</h2>

        <div class="d-flex justify-content-between mb-2">
            <div>
                <pattern-input 
                    @save="on_add_app"
                    placeholder="Type app name..."
                    btnlabel="Add"
                    :regExp="/^[a-z][a-z0-9_]*$/i">
                </pattern-input>
            </div>
            <div>
                <div class="btn-group">
                    <button :class="{active:!ui.apps_compact}" @click="ui.apps_compact=false" class="btn btn-outline-secondary">full</button>
                    <button :class="{active:ui.apps_compact}"  @click="ui.apps_compact=true"  type="button" class="btn btn-outline-secondary">compact</button>
                </div>
            </div>
        </div>

        <app v-for="app in apps" 
            :app="app" 
            :key="app.name" 
            :compact="ui.apps_compact"
            class="mb-2">
        </app>

    </div>
</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import App from './App'
import PatternInput from '../utils/PatternInput'

export default {
    name: 'appsmodels',
    data() {
        return {
            ui: store.project.ui,
        }
    },
    computed: {
        apps() {
            return _.sortBy(store.project.apps, ['name'])
        }
    },
    methods: {
        on_add_app(value) {
            let exist = store.app_get(value)
            if (exist === undefined) {
                store.app_add(value)
            }
            else {
                alert(`Application "${value}" already exist`)
            }
        }
    },
    components: {
        App,
        PatternInput,
    }
}

</script>
