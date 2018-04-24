<template>
    <div class="row">
        <div class="col-4">
            <select v-model="selected_app" class="form-control form-control-sm">
                <option :value="null">Select app...</option>
                <option v-for="app in apps">{{ app.name }}</option>
            </select>
        </div>
        <div class="col" v-show="selected_app">   
            <pattern-input class="new-model"
                @save="add_model"
                style="width: 220px"
                placeholder="Type model name..."
                btnlabel="Add"
                :small="true"
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
                return _.filter(store.project.apps, {'external': false})
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
        },
        components: {
            PatternInput,
        }
    }

</script>