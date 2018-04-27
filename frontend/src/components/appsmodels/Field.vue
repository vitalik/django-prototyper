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
            <field-type :field="field" @focus="on_focus" />
        </td>
        <td class="quickattr"><span @click="toggle('null')" :class="{'badge-warning': field.attrs.null == true, 'badge-light': field.attrs.null == false}" class="badge">N</span></td>
        <td class="quickattr"><span @click="toggle('blank')" :class="{'badge-warning': field.attrs.blank == true, 'badge-light': field.attrs.blank == false}" class="badge">B</span></td>
        <td class="quickattr"><span @click="toggle('unique')" :class="{'badge-warning': field.attrs.unique == true, 'badge-light': field.attrs.unique == false}" class="badge">U</span></td>
        <td class="quickattr"><span @click="toggle('db_index')" :class="{'badge-warning': field.attrs.db_index == true, 'badge-light': field.attrs.db_index == false}" class="badge">&nbsp;I&nbsp;</span></td>
    </tr>
</template>

<script>
import FieldType from './FieldType'

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
            if (this.field.attrs[attr] === undefined)
                this.$set(this.field.attrs, attr, true)
            else
                this.field.attrs[attr] = !this.field.attrs[attr]
        }
    },
    components: {
        FieldType,
    }
}
</script>

<style scoped>
    .bg-light .name {
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

    tr.field td.quickattr .badge-warning {
        opacity: 1;
    }


</style>


