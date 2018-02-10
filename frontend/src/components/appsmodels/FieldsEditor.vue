<template>
    <div>
        <div class="row">
            <div class="col-5">
                <table class="table table-sm table-striped ">
                    <draggable v-model="model.fields" element="tbody">
                        <field v-for="field in model.fields" 
                            @activate="on_field_activate"
                            @activatenext="on_field_next"
                            @activateprev="on_field_prev"
                            :field="field" :key="field.name">
                        </field>
                    </draggable>
                </table>
            </div>
            <div class="col-7">
                <div v-if="active_field" class="card">
                    {{active_field.name}} details
                </div>
                
            </div>
        </div>


        <pattern-input 
            @save="add_field"
            style="width: 250px;"
            placeholder="Type field..."
            btnlabel="Add"
            :regExp="/^[a-z][a-z0-9_]*$/i">
        </pattern-input>

    </div>
</template>

<script>
import { store } from '../../store'
import _ from 'lodash'
import draggable from 'vuedraggable'
import Field from './Field'
import PatternInput from '../utils/PatternInput'

import FieldEvent from './fieldevents'


export default {
    name: 'fieldsediror',
    props: {
        model: {
            required: true,
            type: Object
        }
    },
    data() {
        return {
            active_field: null,
        }
    },
    methods: {
        add_field(name) {
            if (_.find(this.model.fields, {name}) !== undefined) {
                alert(`Field "${name}" already exist.`)
                return
            }
            store.fields_add(this.model.fields, name)
        },
        on_field_activate(field) {
            this.active_field = field
        },
        on_field_next(field) {
            let ind = _.findIndex(this.model.fields, {name:field.name})
            console.info(`Indes of "${field.name}" is ${ind}`)
            ind += 1
            if (ind < this.model.fields.length)
                FieldEvent.activate(this.model.fields[ind].name)
        },
        on_field_prev(field) {
            let ind = _.findIndex(this.model.fields, {name:field.name})
            console.info(`Indes of "${field.name}" is ${ind}`)
            ind -= 1
            if (ind >= 0)
                FieldEvent.activate(this.model.fields[ind].name)
        }
    },
    components: {
        draggable,
        Field,
        PatternInput,
    }
}
</script>
