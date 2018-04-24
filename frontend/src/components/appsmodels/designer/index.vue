<template>
    <div class="h-100">

        <div class="p-1" style="margin-top: -1rem; border-bottom: 1px solid #ccc; background-color: #eee;">
            <button @click="add_model_popup=true" class="btn btn-sm btn-primary mr-4">Add model(s)...</button>
            <button @click="edit_colors_popup=true" class="btn btn-sm btn-outline-secondary" title="Change colors"><i class="fas fa-paint-brush"></i></button>
            <button @click="autosort" class="btn btn-sm btn-outline-secondary" title="Auto sort"><i class="fas fa-list"></i></button>
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
        },
        components: {
            DragArea,
            AppColors,
            Modal,
            AddModelDialog,
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
        box-shadow: 1px 1px 4px ", " #ccc;
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

