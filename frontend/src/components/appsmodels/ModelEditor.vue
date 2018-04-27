<template>
    <div class="h-100">

        <div class="heading">
            <div class="container-fluid">
                <h2>
                    {{ model.name }}

                    <small style="font-size: 14px;">
                        (
                            <span v-for="m in model.inheritance">
                                {{m}}
                            </span>
                            <span v-if="model.inheritance === undefined || model.inheritance.length == 0" class="text-muted">models.Model</span>
                        )
                        <button @click="show_inheritance=true" class="btn btn-sm btn-outline-secondary ml-2">...</button>
                    </small> 

                    <button @click="delete_model" class="btn btn-link text-danger"><i class="far fa-trash-alt"></i></button>


                    <button @click="go_to_model(1)" class="btn btn-sm btn-outline-secondary float-right ml-1"><i class="fas fa-chevron-right"></i></button>
                    <button @click="go_to_model(-1)" class="btn btn-sm btn-outline-secondary float-right"><i class="fas fa-chevron-left"></i></button>
                </h2>
            </div>
        </div>

        <div class="container-fluid h-100 pt-2" style="background-color: #f5f5f5; margin-top: -1rem;">
            <div class="row">
                <div class="col-6">
                    <div class="bg-white p-2">
                        <strong>Fields</strong>

                        <hr>

                        <table class="table table-sm">
                            <draggable v-model="model.fields" element="tbody">
                                <field v-for="(field, pos) in model.fields" 
                                    @activate="on_field_activate"
                                    @activatenext="on_field_next"
                                    @activateprev="on_field_prev"
                                    :class="{'bg-light': active_field && active_field.name == field.name}"
                                    :field="field" 
                                    :pos="pos"
                                    :id="'f_' + pos"
                                    :key="pos">
                                </field>
                            </draggable>
                        </table>

                        <div v-if="model.fields.length == 0" class="mb-4">
                            0 fields.
                        </div>

                        <hr>
                        
                        <pattern-input 
                            @save="add_field"
                            style="width: 250px;"
                            placeholder="Type field..."
                            btnlabel="Add"
                            :regExp="/^[a-z]([a-z0-9_]*[a-z0-9])?$/i">
                        </pattern-input>
                    </div>
                    

                    <meta-editor :model="model" class="mt-4" />
                </div>
                <div class="col-6 col-lg-4">
                    <div v-if="active_field" class="card">
                        <field-attrs-editor :field="active_field" class="card-body" />
                    </div>
                </div>
            </div>
        </div>

        <inheritance v-show="show_inheritance" :model="model" @close="show_inheritance=false" />
    </div>

</template>

<script>
import { store } from '../../store'
import _ from 'lodash'
import draggable from 'vuedraggable'
import FieldAttrsEditor from './FieldAttrsEditor'
import Field from './Field'
import MetaEditor from './MetaEditor'
import Inheritance from './Inheritance'
import PatternInput from '../utils/PatternInput'

export default {
    name: 'modeleditor',
    data() {
        return {
            active_field: null,
            show_inheritance: false,
        }
    },
    computed: {
        app() {
            return store.app_get(this.$route.params.app)
        },
        model() {
            return store.models_get(this.app.name, this.$route.params.model)
        },
        route_field() {
            return _.find(this.model.fields, {name:this.$route.params.field})
        },
    },
    watch: {
        '$route' (to, from) {
            if (this.route_field !== undefined) {
                this.active_field = this.route_field
            } else {
                this.active_field = null
            }
        }
    },
    methods: {
        go_to_model(pos) {
            let keys = store.models_keys(true) // true - skip_exernal
            let ind = _.indexOf(keys, `${this.app.name}.${this.model.name}`) + pos
            if (ind < 0) ind = keys.length-1
            if (ind >= keys.length) ind = 0
            let key = keys[ind].split('.')
            this.$router.push({name: 'model', params: {app: key[0], model:key[1]}})
        },
        add_field(name) {
            if (store.fields_get(this.model, name) !== undefined) {
                alert(`Field "${name}" already exist.`)
                return
            }
            this.active_field = store.fields_add(this.model.fields, name)
        },
        delete_model() {
            store.models_delete(this.app.name, this.model.name)
            this.$router.push('/apps/')
        },
        on_field_activate(field) {
            this.active_field = field
        },
        on_field_next(pos) {
            let ind = pos + 1
            if (ind < this.model.fields.length)
                document.querySelector(`#f_${ind} input`).focus()
        },
        on_field_prev(pos) {
            let ind = pos - 1
            if (ind >= 0)
                document.querySelector(`#f_${ind} input`).focus()
        }
    },
    components: {
        draggable,
        FieldAttrsEditor,
        Field,
        PatternInput,
        MetaEditor,
        Inheritance,
    }
}
</script>
