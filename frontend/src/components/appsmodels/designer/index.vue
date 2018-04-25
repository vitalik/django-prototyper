<template>
    <div class="h-100">

        <div class="p-1" style="margin-top: -1rem; border-bottom: 1px solid #ccc; background-color: #eee;">
            <div class="container-fluid">
                <button @click="add_model_popup=true" class="btn btn-sm btn-primary mr-4">Add model(s)...</button>
                <button @click="edit_colors_popup=true" class="btn btn-sm btn-outline-secondary" title="Change colors"><i class="fas fa-paint-brush"></i></button>
                <button @click="autosort" class="btn btn-sm btn-outline-secondary" title="Auto sort"><i class="fas fa-list"></i></button>
            </div>

        </div>

        <div class="designer h-100">
            <drag-area />
        </div>


        <modal v-show="edit_colors_popup" title="App colours" @close="edit_colors_popup=false" class="appcolors">
            <app-colors/>
        </modal>

        <modal v-show="add_model_popup" title="Add app/model.." @close="add_model_popup=false" class="appcolors">
            <add-model-dialog />
        </modal>
    </div>
</template>

<script>

    import _ from 'lodash'
    import {store} from '../../../store'
    import DragArea from './DragArea'
    import AppColors from './AppColors'
    import AddModelDialog from './AddModelDialog'
    import Modal from '../../utils/Modal'


    export default {
        name: 'modeldesigner',
        data() {
            return {
                edit_colors_popup: false,
                add_model_popup: false,
            }
        },
        computed: {
            apps() {
                return _.orderBy(store.project.apps, ['external', 'name'], ['desc', 'asc'])
            }
        },
        methods: {
            autosort() {
                let x = 20
                let y = 20
                let external_done = false
                _.each(this.apps, (app) => {
                    if (app.models.length == 0)
                        return
                    
                    if (!external_done && !app.external) {
                        y = 20
                        x += 160
                        external_done = true
                    }

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
        },
        components: {
            DragArea,
            AppColors,
            Modal,
            AddModelDialog,
        }
    }

</script>

