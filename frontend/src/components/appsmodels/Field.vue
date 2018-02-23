<template>
    <tr class="field">
        <td>
            <input 
                v-model.lazy="field.name"
                @focus="on_focus" 
                @keydown.down="on_keydown"
                @keydown.up="on_keyup"
                ref="textinput"
                class="name">
        </td>
        <td>
            <select v-model="field.type" style="width: 100%;" @focus="on_focus">
                <option v-for="t in field_choices">{{t}}</option>
            </select>
        </td>
        <td class="quickattr"><span @click="toggle('null')" :class="{'badge-primary': field.null == true, 'badge-light': field.null == false}" class="badge">N</span></td>
        <td class="quickattr"><span @click="toggle('blank')" :class="{'badge-primary': field.blank == true, 'badge-light': field.blank == false}" class="badge">B</span></td>
        <td class="quickattr"><span @click="toggle('unique')" :class="{'badge-primary': field.unique == true, 'badge-light': field.unique == false}" class="badge">U</span></td>
        <td class="quickattr"><span @click="toggle('db_index')" :class="{'badge-primary': field.db_index == true, 'badge-light': field.db_index == false}" class="badge">&nbsp;I&nbsp;</span></td>
    </tr>
</template>

<script>
import _ from 'lodash'
import {FIELDS} from '../../django/fields'

export default {
    name: 'field',
    props: {
        field: {
            required: true,
            type: Object
        },
        pos: {
            required: true,
            type: Number
        }
    },
    computed: {
        field_choices() {
            return _.keys(FIELDS)
        }
    },
    methods: {
        on_focus() {
            this.$emit('activate', this.field)
        },
        on_keydown() {
            this.$emit('activatenext', this.pos)
        },
        on_keyup() {
            this.$emit('activateprev', this.pos)
        },
        toggle(attr) {
            this.$emit('activate', this.field)
            if (this.field[attr] === undefined)
                this.$set(this.field, attr, true)
            else
                this.field[attr] = !this.field[attr]
        }
    }
}
</script>

<style scoped>
    .table-primary .name {
        background-color: white !important;
    }
    .name {
        border: none;
        background: transparent;
        width: 100%;
    }
    tr.field td {
        border: none;
    }
    tr.field .badge {
        cursor: pointer;
    }
    tr.field td.quickattr {
        padding: 0px;
    }

    tr.field td.quickattr .badge {
        opacity: 0.3;
    }

    tr.field td.quickattr .badge-primary {
        opacity: 1;
    }


</style>


