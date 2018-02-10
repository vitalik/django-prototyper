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
            
            <select style="width: 100%;" @focus="on_focus">
                <option>{{field.type}}</option>
            </select>
        </td>
    </tr>
</template>

<script>

import FieldEvent from './fieldevents'

export default {
    name: 'field',
    props: {
        field: {
            required: true,
            type: Object
        }
    },
    mounted() {
        FieldEvent.on_activate((field_name) => {
            if (this.field.name == field_name) {
                this.$refs.textinput.focus()
            }
        })
    },
    beforeDestroy() {
        FieldEvent.unsubscribe()
    },
    methods: {
        on_focus() {
            this.$emit('activate', this.field)
        },
        on_keydown() {
            this.$emit('activatenext', this.field)
        },
        on_keyup() {
            this.$emit('activateprev', this.field)
        }
    }
}
</script>

<style scoped>
    .name {
        border: none;
        background: transparent;
    }
    tr.field td {
        border: none;
    }

</style>


