<template>
    <div class="card h-100">
        <div class="card-header">
            <button @click="autosort" class="btn btn-secondary">Auto sort</button>
        </div>
        <div class="card-body designer h-100">
            
            <model v-for="item in models" 
                    class="model"
                    :key="item.app.name + '.' + item.model.name"
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


export default {
    name: 'modeldesigner',
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
                    result.push({app: app, model: m})
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
        }
    },
    components: {
        Model,
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
    .designer .model.active {
        box-shadow: 1px 1px 4px", "#ccc;
        z-index: 100;
        margin-left: -4px;
        margin-top: -4px;
        padding-left: 8px;
        padding-top: 6px;
        box-shadow: 0px 0px 4px #ccc;
    }
</style>

