<template>
    <div>
        <div class="row">
            <div class="col-4">
                Select application
                <select v-model="selected_app" class="form-control">
                    <option :value="null">Select app...</option>
                    <option v-for="app in apps">{{ app.name }}</option>
                    <option :value="false"> + Create new app</option>
                </select>
            </div>
            <div class="col" v-show="selected_app">
                New model
                <pattern-input class="new-model"
                    @save="add_model"
                    style="width: 220px"
                    placeholder="Type model name..."
                    btnlabel="Add"
                    :regExp="/^[a-z]([a-z0-9_]*[a-z0-9])?$/i">
                </pattern-input>
            </div>
        </div>


        <div v-if="selected_app === false">
            New app
            <pattern-input
                @save="add_app"
                style="width: 250px"
                placeholder="Type application name..."
                btnlabel="Add"
                :regExp="/^[a-z]([a-z0-9_]*[a-z0-9])?$/i">
            </pattern-input>
        </div>


    </div>
</template>


<script>
    import _ from 'lodash'
    import {store} from '../../../store'
    import PatternInput from '../../utils/PatternInput'

    export default {
        name: 'addmodeldialog',
        data() {
            return {
                selected_app: null,
            }
        },
        computed: {
            apps() {
                let items = _.filter(store.project.apps, {'external': false})
                return _.sortBy(items, ['name'])
            },
        },
        methods: {
            add_model(name) {
                if (store.models_get(this.selected_app, name) !== undefined) {
                    alert(`Model "${name}" already exist`)
                    return
                }
                store.models_add(this.selected_app, name)
            },
            add_app(name) {
                if (store.app_get(name) !== undefined) {
                    alert(`application "${name}" already exist`)
                    return
                }
                store.app_add(name)
                this.selected_app = name
            }
        },
        components: {
            PatternInput,
        }
    }

</script>