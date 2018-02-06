<template>
    <div>
        <table class="table table-sm">
            <draggable v-model="model.fields" element="tbody">
                <field v-for="field in model.fields" 
                    :field="field" key="field.name">
                </field>
            </draggable>
            <tr>
                <td style="width: 250px;">
                    <pattern-input 
                        @save="add_field"
                        placeholder="Type field..."
                        btnlabel="Add"
                        :regExp="/^[a-z][a-z0-9_]*$/i">
                    </pattern-input>
                </td>
                <td></td>
            </tr>
        </table>

    </div>
</template>

<script>
import { store } from '../../store'
import _ from 'lodash'
import draggable from 'vuedraggable'
import Field from './Field'
import PatternInput from '../utils/PatternInput'


export default {
    name: 'fieldsediror',
    props: {
        model: {
            required: true,
            type: Object
        }
    },
    methods: {
        add_field(name) {
            if (_.find(this.model.fields, {name}) !== undefined) {
                alert(`Field "${name}" already exist.`)
                return
            }
            store.fields_add(this.model.fields, name)
        }
    },
    components: {
        draggable,
        Field,
        PatternInput,
    }
}
</script>
