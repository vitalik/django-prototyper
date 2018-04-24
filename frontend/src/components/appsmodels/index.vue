<template>
    <div class="h-100">
        <div class="heading">
            <div class="container-fluid">
                <div class="row">
                    <div class="col">
                        <h2>Apps and Models</h2>
                    </div>
                    <div class="col text-right">
                        <div class="btn-group">
                            <button :class="{active:ui.models_view=='list'}" @click="ui.models_view='list'" class="btn btn-outline-secondary">List</button>
                            <button :class="{active:ui.models_view=='compact'}"  @click="ui.models_view='compact'"  type="button" class="btn btn-outline-secondary">Compact</button>
                            <button :class="{active:ui.models_view=='designer'}"  @click="ui.models_view='designer'"  type="button" class="btn btn-outline-secondary">Designer</button>
                        </div>
                    </div>

                </div>
                
            </div>
        </div>


        



        <model-designer v-if="ui.models_view=='designer'" />

        <div v-if="ui.models_view!='designer'">
            <div class="container-fluid">

                <pattern-input 
                    @save="on_add_app"
                    placeholder="Type app name..."
                    btnlabel="Add"
                    style="max-width: 200px;"
                    class="mb-1"
                    :regExp="/^[a-z]([a-z0-9_]*[a-z0-9])?$/i">
                </pattern-input>

                <app v-for="app in apps" 
                    :app="app" 
                    :key="app.name" 
                    :compact="ui.models_view == 'compact'"
                    class="mb-2">
                </app>

                <div v-if="apps.length == 0">
                    No apps created yet.
                </div>

            </div>
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
            let apps = _.filter(store.project.apps, {'external': false})
            return _.sortBy(apps, ['name'])
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
