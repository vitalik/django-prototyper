<template>
    <div class="h-100">
        <h2>Apps and Models</h2>
        <hr>

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
                    <button :class="{active:ui.models_view=='full'}" @click="ui.models_view='full'" class="btn btn-outline-secondary">full</button>
                    <button :class="{active:ui.models_view=='compact'}"  @click="ui.models_view='compact'"  type="button" class="btn btn-outline-secondary">compact</button>
                    <button :class="{active:ui.models_view=='designer'}"  @click="ui.models_view='designer'"  type="button" class="btn btn-outline-secondary">designer</button>
                </div>
            </div>
        </div>

        <model-designer v-if="ui.models_view=='designer'" />

        <div v-else>
            <app v-for="app in apps" 
                :app="app" 
                :key="app.name" 
                :compact="ui.models_view == 'compact'"
                class="mb-2">
            </app>
        </div>


    </div>
</template>

<script>
import _ from 'lodash'
import { store } from '../../store'
import App from './App'
import ModelDesigner from './designer'
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
        ModelDesigner
    }
}

</script>
