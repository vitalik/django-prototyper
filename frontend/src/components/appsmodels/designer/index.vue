<template>
    <div class="card h-100">
        
        <modal v-show="edit_colors" title="App colours" @close="edit_colors=false" class="appcolors">
            <app-colors />
        </modal>
        
        <div class="card-header">
            {{selected_models}}
            <button @click="edit_colors=true" class="btn btn-secondary float-right ml-2">colors</button>
            <button @click="autosort" class="btn btn-secondary float-right">Auto sort</button>
        </div>
        <div class="card-body designer h-100">

            <model v-for="item in models" 
                    @click.native="select_model(item, $event)"
                    class="model"
                    :class="{selected:item.selected}"
                    :key="item.key"
                    :model="item.model"
                    :app="item.app"
                    :style="{left: item.model.ui_left+'px', top: item.model.ui_top+'px'}" >
            </model>
        </div>
    </div>
</template>

<script>

import _ from 'lodash'
import { store } from '../../../store'
import Model from './Model'
import AppColors from './AppColors'
import Modal from '../../utils/Modal'

export default {
    name: 'modeldesigner',
    data() {
        return {
            edit_colors: false,
            selected_models: [],
        }
    },
    computed: {
        apps() {
            return store.project.apps
        },
        models() {
            let result = []
            let n = 0
            _.each(this.apps, (app) => {
                _.each(app.models, (m) => {
                    if (m.ui_top == undefined) {
                        this.$set(m, 'ui_top', n * 40)
                        this.$set(m, 'ui_left', n * 40)
                    }
                    let key = app.name + '.' + m.name
                    result.push({app: app, model: m, selected: _.indexOf(this.selected_models, key) != -1, key:key})
                    n += 1
                })
            })
            return result
        },
    },
    methods: {
        autosort() {
            let x = 20
            let y = 20
            _.each(this.apps, (app) => {
                _.each(app.models, (m) => {
                    m.ui_top = y
                    m.ui_left = x
                    if (m.fields.length < 5)
                        y += 40 + (22 * m.fields.length)
                    else
                        y += 160
                })
                if (y > 500) {
                    y = 20
                    x += 160
                } else {
                    y += 20
                }
            })
        },
        select_model(item, event) {
            let modifier = event.shiftKey || event.altKey || event.ctrlKey
            if (!modifier)
                this.selected_models = [item.key]
            else
                this.selected_models.push(item.key)
        }
    },
    components: {
        Model,
        AppColors,
        Modal,
    }
}

</script>


<style>
    .designer {
        overflow: scroll;
        position: relative;
    }
    .designer .model {
        padding: 0.1rem 0.3rem;
        position: absolute;
        min-width: 150px;
        border-radius: 2px;
    }
    .designer .model.selected {
        border: 1px solid #00f !important;
        box-shadow: 0px 0px 4px #00f;
    }
    .designer .model.active {
        box-shadow: 1px 1px 4px", "#ccc;
        z-index: 100;
        margin-left: -4px;
        margin-top: -4px;
        padding-left: 8px;
        padding-top: 6px;
        box-shadow: 0px 0px 4px #ccc;
    }
    .appcolors .modal-dialog {
        max-width: 700px;
    }
</style>

