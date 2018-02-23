<template>
    <div class="settings">
        <h2>
            {{ app.name }}.{{ model.name }}
            <button @click="delete_model" class="btn btn-outline-danger float-right">Delete</button>
        </h2>
        <hr>
        <div class="row">
            <div class="col-6">
                <table class="table table-sm table-striped ">
                    <draggable v-model="model.fields" element="tbody">
                        <field v-for="(field, pos) in model.fields" 
                            @activate="on_field_activate"
                            @activatenext="on_field_next"
                            @activateprev="on_field_prev"
                            :class="{'table-primary': active_field && active_field.name == field.name}"
                            :field="field" 
                            :pos="pos"
                            :id="'f_' + pos"
                            :key="pos">
                        </field>
                    </draggable>
                </table>
                
                <pattern-input 
                    @save="add_field"
                    style="width: 250px;"
                    placeholder="Type field..."
                    btnlabel="Add"
                    :regExp="/^[a-z][a-z0-9_]*$/i">
                </pattern-input>

                <meta-editor :model="model" class="mt-4" />
            </div>
            <div class="col-6 col-lg-4">
                <div v-if="active_field" class="card">
                    <div class="card-header"><strong>{{active_field.name}}</strong> = {{active_field.type}}</div>
                    <attrs-editor :field="active_field" class="card-body"></attrs-editor>
                </div>
            </div>
        </div>
    </div>

</template>

<script>
import { store } from '../../store'
import _ from 'lodash'
import draggable from 'vuedraggable'
import AttrsEditor from './AttrsEditor'
import Field from './Field'
import MetaEditor from './MetaEditor'
import PatternInput from '../utils/PatternInput'

export default {
    name: 'modeleditor',
    data() {
        return {
            active_field: null,
        }
    },
    computed: {
        app() {
            return store.app_get(this.$route.params.app)
        },
        model() {
            return store.models_get(this.app.name, this.$route.params.model)
        }
    },
    methods: {
        add_field(name) {
            if (store.fieds_get(this.model, name) !== undefined) {
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
        AttrsEditor,
        Field,
        PatternInput,
        MetaEditor,
    }
}
</script>
