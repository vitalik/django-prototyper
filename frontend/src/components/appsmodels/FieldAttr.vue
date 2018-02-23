<template>
    <tr class="field-attr">
        <td class="text-right text-nowrap" style="width: 150px;">{{attr}} = </td>
        <td>
            <input v-if="attr_value_type == String" v-model.lazy="attr_value" type="text" class="form-control form-control-sm">
            <input v-if="attr_value_type == Number" v-model.lazy="attr_value" type="number" class="form-control form-control-sm" style="width: 60px;">
            <InputTrueFalse v-if="attr_value_type == Boolean" v-model="attr_value" :showdefault="attr_default" class="form-control form-control-sm" />
        </td>
    </tr>
</template>

<script>

import {ATTRIBUTES} from '../../django/fields'
import InputTrueFalse from '../utils/InputTrueFalse'

export default {
    name: 'field-attr',
    props: {
        field: {
            required: true,
            type: Object
        },
        attr: {
            required: true,
            type: String
        }
    },
    data() {
        return {
            attr_value: null,
        }
    },
    mounted() {
        this.attr_value = this.field[this.attr]
    },
    watch: {
        field: {
            handler: function(val) {
                this.attr_value = this.field[this.attr]
            },
            deep: true
        },
        attr_value(value) {
            this.$set(this.field, this.attr, value)
        }
    },
    computed: {
        attr_value_type() {
            return ATTRIBUTES[this.attr]['type']
        },
        attr_default() {
            return ATTRIBUTES[this.attr]['default']
        }
    },
    components: {
        InputTrueFalse,
    }
}
</script>

<style>
    .field-attr .form-control-sm {
        padding: 0.1rem 0.2rem;
    }
    .field-attr select.form-control-sm {
        height: 20px !important;
    }
</style>

